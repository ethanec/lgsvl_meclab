/**
 * Copyright (c) 2019 LG Electronics, Inc.
 *
 * This software contains code licensed as described in LICENSE.
 *
 */

using System.Collections.Generic;
using UnityEngine;
using HD = apollo.hdmap;

namespace Simulator.Map
{
    public interface IMapLaneLineCommon<T> where T : IMapLaneLineCommon<T>
    {
        List<T> befores { get; set; }
        List<T> afters { get; set; }
    }

    public class MapLane : MapDataPoints, IMapLaneLineCommon<MapLane>, IMapType
    {
        public bool motorOnly = false;
        public bool vehicleOnly = false;
        public bool displayLane = false;
        public bool needSelfReverseLane = false;
        public bool isSelfReverseLane = false;
        public string otherSelfReverseLaneId = null;

        public float displayLaneWidth = 3.7f; // apollo default lane width

        public List<MapLane> befores { get; set; } = new List<MapLane>();
        public List<MapLane> afters { get; set; } = new List<MapLane>();

        public string id
        {
            get;
            set;
        }

        [System.NonSerialized]
        public MapLane leftLaneForward = null;
        [System.NonSerialized]
        public MapLane rightLaneForward = null;
        [System.NonSerialized]
        public MapLane leftLaneReverse = null;
        [System.NonSerialized]
        public MapLane rightLaneReverse = null;
        [System.NonSerialized]
        public int laneCount;
        [System.NonSerialized]
        public int laneNumber;

        public MapLine leftLineBoundry;
        public MapLine rightLineBoundry;
        public MapLine stopLine;

        public List<MapLane> yieldToLanes = new List<MapLane>(); // TODO calc
        [System.NonSerialized]
        public List<MapLane> nextConnectedLanes = new List<MapLane>();
        [System.NonSerialized]
        public List<MapLane> nextConnectedMotorLanes = new List<MapLane>();
        [System.NonSerialized]
        public List<MapLane> nextConnectedVehicleLanes = new List<MapLane>();
        [System.NonSerialized]
        public List<MapLane> prevConnectedLanes = new List<MapLane>();

        [System.NonSerialized]
        public bool Spawnable = false;
        public bool isTrafficLane { get; set; } = false;
        public bool isStopSignIntersectionLane { get; set; } = false;
        public bool isIntersectionLane { get; set; } = false;

        public LaneTurnType laneTurnType = LaneTurnType.NO_TURN;

        public float speedLimit = 20.0f;

        public override void Draw()
        {
            if (mapLocalPositions.Count < 2) return;

            AnnotationGizmos.DrawWaypoints(transform, mapLocalPositions, MapAnnotationTool.PROXIMITY * 0.5f, laneColor + selectedColor);
            AnnotationGizmos.DrawLines(transform, mapLocalPositions, laneColor + selectedColor);
            AnnotationGizmos.DrawArrowHeads(transform, mapLocalPositions, laneColor + selectedColor);
            if (MapAnnotationTool.SHOW_HELP)
            {
#if UNITY_EDITOR
                UnityEditor.Handles.Label(transform.position, "    LANE " + laneTurnType);
#endif
            }

#if UNITY_EDITOR
            if (UnityEditor.Selection.activeGameObject == this.gameObject && MapAnnotationTool.SHOW_MAP_SELECTED)
            {
                foreach (var yl in yieldToLanes)
                {
                    if (yl != null)
                    {
                        AnnotationGizmos.DrawWaypoints(yl.transform, yl.mapLocalPositions, MapAnnotationTool.PROXIMITY * 0.25f, new Color(1f, 1f, 0f, 0.5f));
                        AnnotationGizmos.DrawLines(yl.transform, yl.mapLocalPositions, new Color(1f, 1f, 0f, 0.5f));
                        AnnotationGizmos.DrawArrowHeads(yl.transform, yl.mapLocalPositions, new Color(1f, 1f, 0f, 0.5f));
                    }
                }
            }
#endif
        }

        public void ReversePoints()
        {
            if (mapLocalPositions.Count < 2) return;

            mapLocalPositions.Reverse();

            // For parking, self-reverse lane should not have same waypoint coordinates.
            for (int i=0; i<mapLocalPositions.Count; i++)
                mapLocalPositions[i] = new Vector3((float)(mapLocalPositions[i].x + 0.1), (float)(mapLocalPositions[i].y + 0.1), (float)(mapLocalPositions[i].z + 0.1));
        }

        public void SetTrigger()
        {
            var colliders = GetComponentsInChildren<BoxCollider>();
            foreach (var col in colliders)
            {
                Destroy(col.gameObject);
            }

            if (mapLocalPositions.Count >= 2)
            {
                for (int i = 0; i < mapLocalPositions.Count - 1; i++)
                {
                    var laneBox = new GameObject("LaneBox");
                    laneBox.layer = LayerMask.NameToLayer("Lane");
                    var boxCollider = laneBox.AddComponent<BoxCollider>();
                    boxCollider.isTrigger = true;
                    boxCollider.size = new Vector3(displayLaneWidth, 10, Vector3.Distance(mapLocalPositions[i], mapLocalPositions[i + 1]));
                    laneBox.transform.position = transform.TransformPoint((mapLocalPositions[i] + mapLocalPositions[i+1]) / 2);
                    laneBox.transform.rotation = Quaternion.LookRotation(Vector3.Normalize(mapWorldPositions[i+1] - mapWorldPositions[i]));
                    laneBox.transform.parent = transform;
                }
            }
        }
    }
}