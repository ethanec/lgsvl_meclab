/**
 * Copyright (c) 2019 LG Electronics, Inc.
 *
 * This software contains code licensed as described in LICENSE.
 *
 */

using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Linq;
using Simulator.Utilities;
using Simulator.Controllable;

namespace Simulator.Map
{
    public class MapSignal : MapData, IControllable, IMapType
    {
        public uint ID;
        public Vector3 boundOffsets = new Vector3();
        public Vector3 boundScale = new Vector3();
        public List<SignalData> signalData = new List<SignalData>();
        public MapLine stopLine;
        public Renderer signalLightMesh;
        public SignalType signalType = SignalType.MIX_3_VERTICAL;
        public Texture EmissionTexture1; // Only 1 circle. It's for red and yellow lights.
        public Texture EmissionTexture2; // There are many types. It's for different situations such as 4LD, 5LDR...
        private Coroutine SignalCoroutine;
        public string id
        {
            get;
            set;
        }

        public string ControlType { get; set; } = "signal";
        public string CurrentState { get; set; }
        public string[] ValidStates { get; set; } = new string[] { "green", "yellow", "red", "black" };
        public string[] ValidActions { get; set; } = new string[] { "trigger", "wait", "loop" };
        public string DefaultControlPolicy { get; set; }
        public string CurrentControlPolicy { get; set; }

        public void Control(List<ControlAction> controlActions)
        {
            var fixedUpdateManager = SimulatorManager.Instance.FixedUpdateManager;

            if (SignalCoroutine != null)
            {
                fixedUpdateManager.StopCoroutine(SignalCoroutine);
                SignalCoroutine = null;
            }

            SignalCoroutine = fixedUpdateManager.StartCoroutine(SignalLoop(controlActions));
        }

        private void OnDestroy()
        {
            Resources.UnloadUnusedAssets();
        }

        public void SetSignalMeshData()
        {
            var signalMeshes = new List<SignalLight>();
            signalMeshes.AddRange(FindObjectsOfType<SignalLight>());
            foreach (var mesh in signalMeshes)
            {                
                if (Vector3.Distance(transform.position, mesh.transform.position) < 0.1f)
                {
                    signalLightMesh = mesh.GetComponent<Renderer>();                    
                    break;
                }
            }
        }

        private Color GetTypeColor(SignalData data)
        {
            Color currentColor = Color.black;
            switch (data.signalColor)
            {
                case SignalColorType.Red:
                    currentColor = Color.red;
                    break;
                case SignalColorType.Yellow:
                    currentColor = Color.yellow;
                    break;
                case SignalColorType.Green:
                    currentColor = Color.green;
                    break;
                default:
                    break;
            }
            return currentColor;
        }

        public void SetSignalState(string state)
        {
            if (!ValidStates.Contains(state))
            {
                Debug.LogError($"'{state}' is an invalid state for '{ControlType}'");
                return;
            }

            CurrentState = state;
            // 4LD = 4 Lights with green_Left + green_Direct
            if (signalLightMesh.name.Contains("4LD") || signalLightMesh.name.Contains("4LR") || signalLightMesh.name.Contains("4DR"))
            {
                signalType = SignalType.MIX_4_VERTICAL;
                switch (CurrentState)
                {                    
                    case "red":
                        stopLine.currentState = SignalLightStateType.Red;
                        signalLightMesh.material.SetTexture("_EmissiveColorMap", EmissionTexture1);
                        // EmissionTexture1 = SignalTrafficVerticalEmissive_4.png
                        signalLightMesh.material.SetTextureOffset("_EmissiveColorMap", new Vector2(0f, 0.7f));
                        signalLightMesh.material.SetColor("_EmissiveColor", Color.red);
                        signalLightMesh.material.SetVector("_EmissiveColor", Color.red * 3.0f);
                        break;
                    case "yellow":
                        stopLine.currentState = SignalLightStateType.Yellow;
                        signalLightMesh.material.SetTexture("_EmissiveColorMap", EmissionTexture1);
                        signalLightMesh.material.SetTextureOffset("_EmissiveColorMap", new Vector2(0f, 0.45f));                        
                        signalLightMesh.material.SetColor("_EmissiveColor", Color.yellow);
                        signalLightMesh.material.SetVector("_EmissiveColor", Color.yellow * 3.0f);
                        break;
                    case "black":
                        stopLine.currentState = SignalLightStateType.Black;
                        signalLightMesh.material.SetColor("_EmissiveColor", Color.black);
                        signalLightMesh.material.SetVector("_EmissiveColor", Color.black * 3.0f);
                        break;
                    case "green":
                        stopLine.currentState = SignalLightStateType.Green;
                        signalLightMesh.material.SetTexture("_EmissiveColorMap", EmissionTexture2); 
                        // We need to change EmissionTexture2 in Shalun.unity for each light.
                        // When signalLightMesh = ~4DR~, EmissionTexture2 = SignalTrafficVerticalEmissive_4DR.png 
                        // When signalLightMesh = ~4LD~, EmissionTexture2 = SignalTrafficVerticalEmissive_4LD.png
                        // When signalLightMesh = ~4LR~, EmissionTexture2 = SignalTrafficVerticalEmissive_4LR.png
                        signalLightMesh.material.SetTextureOffset("_EmissiveColorMap", new Vector2(0f, 0f));                                                                        
                        signalLightMesh.material.SetColor("_EmissiveColor", Color.green);
                        signalLightMesh.material.SetVector("_EmissiveColor", Color.green * 4.0f);
                        break;
                    default:
                        break;
                }                                  
            }
            // 5LDR = 5 lights with red + yellow + green_left + green_direct + green_right.
            else if (signalLightMesh.name.Contains("5LDR"))
            {
                signalType = SignalType.MIX_5_VERTICAL;
                switch (CurrentState)
                {                    
                    case "red":
                        stopLine.currentState = SignalLightStateType.Red;
                        signalLightMesh.material.SetTexture("_EmissiveColorMap", EmissionTexture1);
                        // EmissionTexture1 = SignalTrafficVerticalEmissive_5.png
                        signalLightMesh.material.SetTextureOffset("_EmissiveColorMap", new Vector2(0f, 0.75f));
                        signalLightMesh.material.SetColor("_EmissiveColor", Color.red);
                        signalLightMesh.material.SetVector("_EmissiveColor", Color.red * 3.0f);
                        break;
                    case "yellow":
                        stopLine.currentState = SignalLightStateType.Yellow;
                        signalLightMesh.material.SetTexture("_EmissiveColorMap", EmissionTexture1);
                        signalLightMesh.material.SetTextureOffset("_EmissiveColorMap", new Vector2(0f, 0.56f));                        
                        signalLightMesh.material.SetColor("_EmissiveColor", Color.yellow);
                        signalLightMesh.material.SetVector("_EmissiveColor", Color.yellow * 3.0f);
                        break;
                    case "black":
                        stopLine.currentState = SignalLightStateType.Black;
                        signalLightMesh.material.SetColor("_EmissiveColor", Color.black);
                        signalLightMesh.material.SetVector("_EmissiveColor", Color.black * 3.0f);
                        break;
                    case "green":
                        stopLine.currentState = SignalLightStateType.Green;
                        signalLightMesh.material.SetTexture("_EmissiveColorMap", EmissionTexture2);
                        // EmissionTexture2 = SignalTrafficVerticalEmissive_5LDR.png
                        signalLightMesh.material.SetTextureOffset("_EmissiveColorMap", new Vector2(0f, 0f));                                                                        
                        signalLightMesh.material.SetColor("_EmissiveColor", Color.green);
                        signalLightMesh.material.SetVector("_EmissiveColor", Color.green * 4.0f);
                        break;
                    default:
                        break;
                }                          
            }
            else
            {
                signalType = SignalType.MIX_3_VERTICAL;
                switch (CurrentState)
                {
                    case "red":
                        stopLine.currentState = SignalLightStateType.Red;
                        signalLightMesh.material.SetTextureOffset("_EmissiveColorMap", new Vector2(0f, 0.65f));
                        signalLightMesh.material.SetColor("_EmissiveColor", Color.red);
                        signalLightMesh.material.SetVector("_EmissiveColor", Color.red * 3.0f);
                        break;
                    case "green":
                        stopLine.currentState = SignalLightStateType.Green;
                        signalLightMesh.material.SetTextureOffset("_EmissiveColorMap", new Vector2(0f, 0f));
                        signalLightMesh.material.SetColor("_EmissiveColor", Color.green);
                        signalLightMesh.material.SetVector("_EmissiveColor", Color.green * 3.0f);
                        break;
                    case "yellow":
                        stopLine.currentState = SignalLightStateType.Yellow;
                        signalLightMesh.material.SetTextureOffset("_EmissiveColorMap", new Vector2(0f, 0.35f));
                        signalLightMesh.material.SetColor("_EmissiveColor", Color.yellow);
                        signalLightMesh.material.SetVector("_EmissiveColor", Color.yellow * 3.0f);
                        break;
                    case "black":
                        stopLine.currentState = SignalLightStateType.Black;
                        signalLightMesh.material.SetColor("_EmissiveColor", Color.black);
                        signalLightMesh.material.SetVector("_EmissiveColor", Color.black * 3.0f);
                        break;
                    default:
                        break;
                }
            }
        }

        private IEnumerator SignalLoop(List<ControlAction> controlActions)
        {
            var fixedUpdateManager = SimulatorManager.Instance.FixedUpdateManager;

            for (int i = 0; i < controlActions.Count; i++)
            {
                var action = controlActions[i].Action;
                var value = controlActions[i].Value;
                
                switch (action)
                {
                    case "state":
                        SetSignalState(value);
                        break;
                    case "trigger":
                        if (!float.TryParse(value, out float threshold) || threshold < 0f)
                        {
                            threshold = 0f;
                        }
                        yield return fixedUpdateManager.WaitUntilFixed(() => IsAgentAround(threshold));
                        break;
                    case "wait":
                        if (!float.TryParse(value, out float seconds) || seconds < 0f)
                        {
                            seconds = 0f;
                        }
                        yield return fixedUpdateManager.WaitForFixedSeconds(seconds);
                        break;
                    case "loop":
                        i = -1;
                        break;
                    default:
                        Debug.LogError($"'{action}' is an invalid action for '{ControlType}'");
                        break;
                }
            }
        }

        private bool IsAgentAround(float threshold)
        {
            var agent = SimulatorManager.Instance.AgentManager.CurrentActiveAgent;
            if (agent == null)
            {
                return false;
            }

            var agentPos = agent.transform.position;
            var signalPos = new Vector3(transform.position.x, agentPos.y, transform.position.z);  // Check distance in xz plane
            var distance = Vector3.Distance(agentPos, signalPos);

            return distance <= threshold;
        }

        public System.ValueTuple<Vector3, Vector3, Vector3, Vector3> Get2DBounds()
        {
            var matrix = transform.localToWorldMatrix * Matrix4x4.TRS(boundOffsets, Quaternion.identity, Vector3.Scale(Vector3.one, boundScale));

            float min = boundScale[0];
            int index = 0;
            for (int i = 0; i < 3; i++)
            {
                if (boundScale[i] < min)
                {
                    min = boundScale[i];
                    index = i;
                }
            }

            if (index == 0)
            {
                return ValueTuple.Create(
                    matrix.MultiplyPoint(new Vector3(0, 0.5f, 0.5f)),
                    matrix.MultiplyPoint(new Vector3(0, -0.5f, 0.5f)),
                    matrix.MultiplyPoint(new Vector3(0, -0.5f, -0.5f)),
                    matrix.MultiplyPoint(new Vector3(0, 0.5f, -0.5f))
                    );
            }
            else if (index == 1)
            {
                return ValueTuple.Create(
                    matrix.MultiplyPoint(new Vector3(0.5f, 0, 0.5f)),
                    matrix.MultiplyPoint(new Vector3(-0.5f, 0, 0.5f)),
                    matrix.MultiplyPoint(new Vector3(-0.5f, 0, -0.5f)),
                    matrix.MultiplyPoint(new Vector3(0.5f, 0, -0.5f))
                    );
            }
            else
            {
                return ValueTuple.Create(
                    matrix.MultiplyPoint(new Vector3(0.5f, 0.5f, 0)),
                    matrix.MultiplyPoint(new Vector3(-0.5f, 0.5f, 0)),
                    matrix.MultiplyPoint(new Vector3(-0.5f, -0.5f, 0)),
                    matrix.MultiplyPoint(new Vector3(0.5f, -0.5f, 0))
                    );
            }
        }

        public override void Draw()
        {
            if (signalData == null || signalData.Count < 1) return;

            var lightLocalPositions = signalData.Select(x => x.localPosition).ToList();
            var lightCount = lightLocalPositions.Count;

            // lights
            if (MapAnnotationTool.SHOW_HELP)
            {
#if UNITY_EDITOR
                UnityEditor.Handles.Label(transform.position, "    SIGNAL");
#endif
            }
            for (int i = 0; i < lightCount; i++)
            {
                var start = transform.TransformPoint(lightLocalPositions[i]);
                var end = start + transform.forward * 2f * (1 / MapAnnotationTool.EXPORT_SCALE_FACTOR); // TODO why is this 1/export scale?

                var signalColor = GetTypeColor(signalData[i]) + selectedColor;

                AnnotationGizmos.DrawWaypoint(start, MapAnnotationTool.PROXIMITY * 0.15f, signalColor);
                Gizmos.color = signalColor;
                Gizmos.DrawLine(start, end);
                AnnotationGizmos.DrawArrowHead(start, end, signalColor, arrowHeadScale: MapAnnotationTool.ARROWSIZE, arrowPositionRatio: 1f);
            }

            // stopline
            if (stopLine != null)
            {
                Gizmos.color = Color.magenta;
                Gizmos.DrawLine(transform.position, stopLine.transform.position);
                AnnotationGizmos.DrawArrowHead(transform.position, stopLine.transform.position, Color.magenta, arrowHeadScale: MapAnnotationTool.ARROWSIZE, arrowPositionRatio: 1f);
                if (MapAnnotationTool.SHOW_HELP)
                {
#if UNITY_EDITOR
                    UnityEditor.Handles.Label(stopLine.transform.position, "    STOPLINE");
#endif
                }
            }

            // bounds
            Gizmos.matrix = transform.localToWorldMatrix * Matrix4x4.TRS(Vector3.zero, Quaternion.identity, Vector3.Scale(Vector3.one, boundScale));
            Gizmos.color = Color.red;
            Gizmos.DrawWireCube(Vector3.zero, Vector3.one);
            if (MapAnnotationTool.SHOW_HELP)
            {
#if UNITY_EDITOR
                UnityEditor.Handles.Label(transform.position + Vector3.up, "    SIGNAL BOUNDS");
#endif
            }
        }
    }
}
