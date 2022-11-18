/**
 * Copyright (c) 2019 LG Electronics, Inc.
 *
 * This software contains code licensed as described in LICENSE.
 *
 */

using System;
using System.Text;
using System.Linq;
using System.Collections.Generic;
using UnityEngine;
using Simulator;
using Simulator.Sensors;
using Simulator.Utilities;
using Simulator.Components;
using Simulator.Database;
using SimpleJSON;
using PetaPoco;
using YamlDotNet.Serialization;
using ICSharpCode.SharpZipLib.Zip;

public class AgentManager : MonoBehaviour
{
    public GameObject CurrentActiveAgent { get; private set; } = null;
    public AgentController CurrentActiveAgentController { get; private set; } = null;
    public List<GameObject> ActiveAgents { get; private set; } = new List<GameObject>();

    public event Action<GameObject> AgentChanged;

    public GameObject SpawnAgent(AgentConfig config)
    {
        var go = Instantiate(config.Prefab);
        go.name = config.Name;
        var agentController = go.GetComponent<AgentController>();
        agentController.Config = config;
        SIM.LogSimulation(SIM.Simulation.VehicleStart, config.Name);
        ActiveAgents.Add(go);
        agentController.GTID = ++SimulatorManager.Instance.GTIDs;

        BridgeClient bridgeClient = null;
        if (config.Bridge != null)
        {
            bridgeClient = go.AddComponent<BridgeClient>();
            bridgeClient.Init(config.Bridge);

            if (config.Connection != null)
            {
                var split = config.Connection.Split(':');
                if (split.Length != 2)
                {
                    throw new Exception("Incorrect bridge connection string, expected HOSTNAME:PORT");
                }
                bridgeClient.Connect(split[0], int.Parse(split[1]));
            }
        }
        SIM.LogSimulation(SIM.Simulation.BridgeTypeStart, config.Bridge != null ? config.Bridge.Name : "None");
        if (!string.IsNullOrEmpty(config.Sensors))
        {
            SetupSensors(go, config.Sensors, bridgeClient);
        }

        agentController.AgentSensors.AddRange(agentController.GetComponentsInChildren<SensorBase>(true));

        go.transform.position = config.Position;
        go.transform.rotation = config.Rotation;
        agentController.Init();

        return go;
    }

    public void SpawnAgents(AgentConfig[] agentConfigs)
    {
        CreateAgentsFromConfigs(agentConfigs);

        if (ActiveAgents.Count > 0)
        {
            SetCurrentActiveAgent(0);
        }
    }

    public void SetupDevAgents()
    {
        ActiveAgents.AddRange(GameObject.FindGameObjectsWithTag("Player"));

        if (ActiveAgents.Count == 0)
        {
            string data = null;
#if UNITY_EDITOR
            data = UnityEditor.EditorPrefs.GetString("Simulator/DevelopmentSettings");
#endif
            if (data != null)
            {
                try
                {
                    var json = JSONNode.Parse(data);
                    var createVehicle = json["CreateVehicle"];
                    var vehicleName = json["VehicleName"];
                    if (createVehicle != null && createVehicle.AsBool && vehicleName != null)
                    {
                        using (var db = DatabaseManager.GetConfig(DatabaseManager.GetConnectionString()).Create())
                        {
                            var sql = Sql.Builder.From("vehicles").Where("name = @0", vehicleName.Value);
                            var vehicle = db.SingleOrDefault<VehicleModel>(sql);
                            if (vehicle == null)
                            {
                                Debug.LogError($"Cannot find '{vehicleName.Value}' vehicle in database!");
                            }
                            else
                            {
                                var bundlePath = vehicle.LocalPath;

                                using (ZipFile zip = new ZipFile(bundlePath))
                                {
                                    Manifest manifest;
                                    ZipEntry entry = zip.GetEntry("manifest");
                                    using (var ms = zip.GetInputStream(entry))
                                    {
                                        int streamSize = (int)entry.Size;
                                        byte[] buffer = new byte[streamSize];
                                        streamSize = ms.Read(buffer, 0, streamSize);
                                        manifest = new Deserializer().Deserialize<Manifest>(Encoding.UTF8.GetString(buffer, 0, streamSize));
                                    }

                                    if (manifest.bundleFormat != BundleConfig.VehicleBundleFormatVersion)
                                    {
                                        throw new Exception("Out of date Vehicle AssetBundle. Please check content website for updated bundle or rebuild the bundle.");
                                    }

                                    var texStream = zip.GetInputStream(zip.GetEntry($"{manifest.bundleGuid}_vehicle_textures"));
                                    var textureBundle = AssetBundle.LoadFromStream(texStream, 0, 1 << 20);

                                    string platform = SystemInfo.operatingSystemFamily == OperatingSystemFamily.Windows ? "windows" : "linux";
                                    var mapStream = zip.GetInputStream(zip.GetEntry($"{manifest.bundleGuid}_vehicle_main_{platform}"));
                                    var vehicleBundle = AssetBundle.LoadFromStream(mapStream, 0, 1 << 20);

                                    if (vehicleBundle == null)
                                    {
                                        throw new Exception($"Failed to load '{bundlePath}' vehicle asset bundle");
                                    }

                                    try
                                    {
                                        var vehicleAssets = vehicleBundle.GetAllAssetNames();
                                        if (vehicleAssets.Length != 1)
                                        {
                                            throw new Exception($"Unsupported '{bundlePath}' vehicle asset bundle, only 1 asset expected");
                                        }

                                        // TODO: make this async
                                        if (!AssetBundle.GetAllLoadedAssetBundles().Contains(textureBundle))
                                        {
                                            textureBundle.LoadAllAssets();
                                        }

                                        var prefab = vehicleBundle.LoadAsset<GameObject>(vehicleAssets[0]);
                                        var config = new AgentConfig()
                                        {
                                            Name = vehicle.Name,
                                            Prefab = prefab,
                                            Sensors = vehicle.Sensors,
                                            Connection = json["Connection"].Value,
                                        };
                                        if (!string.IsNullOrEmpty(vehicle.BridgeType))
                                        {
                                            config.Bridge = Simulator.Web.Config.Bridges.Find(bridge => bridge.Name == vehicle.BridgeType);
                                            if (config.Bridge == null)
                                            {
                                                throw new Exception($"Bridge {vehicle.BridgeType} not found");
                                            }
                                        }

                                        var spawn = FindObjectsOfType<SpawnInfo>().OrderBy(s => s.name).FirstOrDefault();
                                        config.Position = spawn != null ? spawn.transform.position : Vector3.zero;
                                        config.Rotation = spawn != null ? spawn.transform.rotation : Quaternion.identity;

                                        SpawnAgent(config);
                                    }
                                    finally
                                    {
                                        textureBundle.Unload(false);
                                        vehicleBundle.Unload(false);
                                    }
                                }
                            }
                        }
                    }
                }
                catch (Exception ex)
                {
                    Debug.LogException(ex);
                }
            }
        }
        else
        {
            var go = ActiveAgents[0];

            var bridgeClient = go.AddComponent<BridgeClient>();
            bridgeClient.Init(new Simulator.Bridge.Ros.RosApolloBridgeFactory());
            bridgeClient.Connect("localhost", 9090);

            SetupSensors(go, DefaultSensors.Apollo30, bridgeClient);
        }

        ActiveAgents.ForEach(agent => agent.GetComponent<AgentController>().Init());

        SetCurrentActiveAgent(0);
    }

    public void SetCurrentActiveAgent(GameObject agent)
    {
        Debug.Assert(agent != null);
        for (int i = 0; i < ActiveAgents.Count; i++)
        {
            if (ActiveAgents[i] == agent)
            {
                SetCurrentActiveAgent(i);
                break;
            }
        }
    }

    public void SetCurrentActiveAgent(int index)
    {
        if (ActiveAgents.Count == 0) return;
        if (index < 0 || index > ActiveAgents.Count - 1) return;
        if (ActiveAgents[index] == null) return;

        CurrentActiveAgent = ActiveAgents[index];
        CurrentActiveAgentController = CurrentActiveAgent.GetComponent<AgentController>();

        foreach (var agent in ActiveAgents)
        {
            agent.GetComponent<AgentController>().Active = (agent == CurrentActiveAgent);
        }
        ActiveAgentChanged(CurrentActiveAgent);
    }

    public void SetNextCurrentActiveAgent()
    {
        var index = GetCurrentActiveAgentIndex();
        index = index < ActiveAgents.Count - 1 ? index + 1 : 0;
        SetCurrentActiveAgent(index);
    }

    public bool GetIsCurrentActiveAgent(GameObject agent)
    {
        return agent == CurrentActiveAgent;
    }

    public int GetCurrentActiveAgentIndex()
    {
        int index = 0;
        for (int i = 0; i < ActiveAgents.Count; i++)
        {
            if (ActiveAgents[i] == CurrentActiveAgent)
                index = i;
        }
        return index;
    }

    public float GetDistanceToActiveAgent(Vector3 pos)
    {
        return Vector3.Distance(CurrentActiveAgent.transform.position, pos);
    }

    private void ActiveAgentChanged(GameObject agent)
    {
        AgentChanged?.Invoke(agent);
    }

    public void ResetAgent()
    {
        CurrentActiveAgent?.GetComponent<AgentController>()?.ResetPosition();
    }

    public void DestroyAgent(GameObject go)
    {
        ActiveAgents.RemoveAll(x => x == go);
        Destroy(go);

        if (ActiveAgents.Count == 0)
        {
            SimulatorManager.Instance.CameraManager.SetFreeCameraState();
        }
        else
        {
            SetCurrentActiveAgent(0);
        }
    }

    public void Reset()
    {
        List<GameObject> agents = new List<GameObject>(ActiveAgents);
        foreach (var agent in agents)
        {
            DestroyAgent(agent);
        }

        ActiveAgents.Clear();
    }

    static string GetSensorType(SensorBase sensor)
    {
        var type = sensor.GetType().GetCustomAttributes(typeof(SensorType), false)[0] as SensorType;
        return type.Name;
    }

    public void SetupSensors(GameObject agent, string sensors, BridgeClient bridgeClient)
    {
        var available = Simulator.Web.Config.Sensors.ToDictionary(sensor => sensor.Name);
        var prefabs = Simulator.Web.Config.SensorPrefabs.ToDictionary(sensor => GetSensorType(sensor));

        var parents = new Dictionary<string, GameObject>()
        {
            { string.Empty, agent },
        };

        var requested = JSONNode.Parse(sensors).Children.ToList();
        while (requested.Count != 0)
        {
            int requestedCount = requested.Count;

            foreach (var parent in parents.Keys.ToArray())
            {
                var parentObject = parents[parent];

                for (int i = 0; i < requested.Count; i++)
                {
                    var item = requested[i];
                    if (item["parent"].Value == parent)
                    {
                        var name = item["name"].Value;
                        var type = item["type"].Value;

                        SensorConfig config;
                        if (!available.TryGetValue(type, out config))
                        {
                            throw new Exception($"Unknown sensor type {type} for {gameObject.name} vehicle");
                        }

                        var sensor = CreateSensor(agent, parentObject, prefabs[type].gameObject, item);
                        sensor.GetComponent<SensorBase>().Name = name;
                        sensor.name = name;
                        SIM.LogSimulation(SIM.Simulation.SensorStart, name);
                        if (bridgeClient != null)
                        {
                            sensor.GetComponent<SensorBase>().OnBridgeSetup(bridgeClient.Bridge);
                        }

                        parents.Add(name, sensor);
                        requested.RemoveAt(i);
                        i--;
                    }
                }
            }

            if (requestedCount == requested.Count)
            {
                throw new Exception($"Failed to create {requested.Count} sensor(s), cannot determine parent-child relationship");
            }
        }
    }

    GameObject CreateSensor(GameObject agent, GameObject parent, GameObject prefab, JSONNode item)
    {
        Vector3 position;
        Quaternion rotation;

        var transform = item["transform"];
        if (transform == null)
        {
            position = parent.transform.position;
            rotation = parent.transform.rotation;
        }
        else
        {
            position = parent.transform.TransformPoint(transform.ReadVector3());
            rotation = parent.transform.rotation * Quaternion.Euler(transform.ReadVector3("pitch", "yaw", "roll"));
        }

        var sensor = Instantiate(prefab, position, rotation, agent.transform);

        var sb = sensor.GetComponent<SensorBase>();
        var sbType = sb.GetType();

        foreach (var param in item["params"])
        {
            var key = param.Key;
            var value = param.Value;

            var field = sbType.GetField(key);
            if (field == null)
            {
                throw new Exception($"Unknown {key} parameter for {item["name"].Value} sensor on {gameObject.name} vehicle");
            }

            if (field.FieldType.IsEnum)
            {
                try
                {
                    var obj = Enum.Parse(field.FieldType, value.Value);
                    field.SetValue(sb, obj);
                }
                catch (ArgumentException ex)
                {
                    throw new Exception($"Failed to set {key} field to {value.Value} enum value for {gameObject.name} vehicle, {sb.Name} sensor", ex);
                }
            }
            else if (field.FieldType == typeof(Color))
            {
                if (ColorUtility.TryParseHtmlString(value.Value, out var color))
                {
                    field.SetValue(sb, color);
                }
                else
                {
                    throw new Exception($"Failed to set {key} field to {value.Value} color for {gameObject.name} vehicle, {sb.Name} sensor");
                }
            }
            else if (field.FieldType == typeof(bool))
            {
                field.SetValue(sb, value.AsBool);
            }
            else if (field.FieldType == typeof(int))
            {
                field.SetValue(sb, value.AsInt);
            }
            else if (field.FieldType == typeof(float))
            {
                field.SetValue(sb, value.AsFloat);
            }
            else if (field.FieldType == typeof(string))
            {
                field.SetValue(sb, value.Value);
            }
            else if (field.FieldType.IsGenericType && field.FieldType.GetGenericTypeDefinition() == typeof(List<>))
            {
                var type = field.FieldType.GetGenericArguments()[0];
                Type listType = typeof(List<>).MakeGenericType(new[] { type });
                System.Collections.IList list = (System.Collections.IList)Activator.CreateInstance(listType);

                foreach(var elemValue in value)
                {
                    var elem = Activator.CreateInstance(type);

                    foreach (var elemField in type.GetFields())
                    {
                        var name = elemField.Name;

                        if (elemValue.Value[name].IsNumber)
                        {
                            elemField.SetValue(elem, elemValue.Value[name].AsFloat);
                        }
                        else if (elemValue.Value[name].IsString)
                        {
                            elemField.SetValue(elem, elemValue.Value[name].Value);
                        }
                    }
                    list.Add(elem);
                }

                field.SetValue(sb, list);
            }
            else
            {
                throw new Exception($"Unknown {field.FieldType} type for {key} field for {gameObject.name} vehicle, {sb.Name} sensor");
            }
        }

        return sensor;
    }

    private void CreateAgentsFromConfigs(AgentConfig[] agentConfigs)
    {
        var spawns = FindObjectsOfType<SpawnInfo>();
        var positions = spawns.OrderBy(spawn => spawn.name).Select(s => s.transform.position).ToArray();
        var rotations = spawns.OrderBy(spawn => spawn.name).Select(s => s.transform.rotation).ToArray();

        // TODO: In case of spawn point absense on the map
        // we have to do educated guess about default spawn point.
        //
        // The best would be to take meshes tagged as Road and
        // find any point on the surface regarless of the altitude.
        // But for now we use zero.
        int count = positions.Length;
        if (count == 0)
        {
            count = 1;
            positions = new [] { Vector3.zero };
            rotations = new [] { Quaternion.identity };
        }

        var renderers = new List<Renderer>();

        for (int current = 0; current < agentConfigs.Length; current++)
        {
            var config = agentConfigs[current];
            config.Position = positions[current % count];
            config.Rotation = rotations[current % count];

            var agent = SpawnAgent(config);

            // offset current spawn point by agent boundaries
            // in order to place next agent on top of current one
            agent.GetComponentsInChildren(renderers);
            var bounds = new Bounds(config.Position, Vector3.zero);
            renderers.ForEach(renderer => bounds.Encapsulate(renderer.bounds));

            positions[current % count] += Vector3.up * bounds.size.y;
        }
    }
}
