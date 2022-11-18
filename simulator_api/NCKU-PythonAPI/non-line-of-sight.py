# -*- coding: utf-8 -*-
import os
import lgsvl
import time

def waypoint_minus(waypoint_a, waypoint_b, interval):
  # print("waypoint a :", waypoint_a.position.x, ", ", waypoint_a.position.y, ", ", waypoint_a.position.z, ", ", waypoint_a.angle.y)
  x = (waypoint_b.position.x - waypoint_a.position.x)/interval
  y = (waypoint_b.position.y - waypoint_a.position.y)/interval
  z = (waypoint_b.position.z - waypoint_a.position.z)/interval
  yaw = (waypoint_b.angle.y - waypoint_a.angle.y)/interval
  vec = [x, y, z, yaw]
  return vec

def smooth(waypoints, interval): #Interpolation
  smooth_waypoints = []
  x = waypoints[0].position.x
  y = waypoints[0].position.y
  z = waypoints[0].position.z
  yaw = waypoints[0].angle.y
  smooth_waypoints.append(lgsvl.DriveWaypoint(lgsvl.Vector(x,y,z), 6, lgsvl.Vector(0, yaw, 0), 0, True, 0))
  for i in range(len(waypoints)-1):
    waypoint_vec = waypoint_minus(waypoints[i], waypoints[i+1], interval)
    for j in range(interval):
      x = x + waypoint_vec[0]
      y = y + waypoint_vec[1]
      z = z + waypoint_vec[2]
      yaw = yaw + waypoint_vec[3]
      smooth_waypoints.append(lgsvl.DriveWaypoint(lgsvl.Vector(x,y,z), 6, lgsvl.Vector(0, yaw, 0), 0, True, 0))
  return smooth_waypoints

# Load Map
sim = lgsvl.Simulator(os.environ.get("SIMULATOR_HOST", "127.0.0.1"), 8181)
if sim.current_scene == "Shalun":
  sim.reset()
else:
  sim.load("Shalun")
spawns = sim.get_spawn()

# ego Vehicle
state = lgsvl.AgentState()
state.transform.position.x = 6769.801
state.transform.position.y = -63.11819
state.transform.position.z = -8162.083
state.transform.rotation.y = 154.54
ego = sim.add_agent("NCKU-Lincoln_MKZ", lgsvl.AgentType.EGO, state)

# ego vehicle attach Autoware IP and Port
connect = input("Connect to autoware y (yes), n (no) :")
if connect == "y":
  ego.connect_bridge(os.environ.get("BRIDGE_HOST", "192.168.0.147"), 9090)
  print("Waiting for connection...")
  while not ego.bridge_connected:
    print("Bridge connecting...")
    time.sleep(1)
  print("Bridge connected:", ego.bridge_connected)

# NPC Vehicle
waypoints = [lgsvl.DriveWaypoint(lgsvl.Vector(6781.964, -63.11819, -8195.831), 0, lgsvl.Vector(0, 154.07, 0), 0, True, 0)]
smooth_waypoints = smooth(waypoints, 5)
state.transform.position = smooth_waypoints[0].position
state.transform.rotation = smooth_waypoints[0].angle
npc1 = sim.add_agent('SchoolBus', lgsvl.AgentType.NPC, state)
npc1.follow(smooth_waypoints,loop=True)

waypoints = [lgsvl.DriveWaypoint(lgsvl.Vector(6794.414, -63.11819, -8201.563), 0, lgsvl.Vector(0, -116.422, 0), 0, True, 0)]
smooth_waypoints = smooth(waypoints, 5)
state.transform.position = smooth_waypoints[0].position
state.transform.rotation = smooth_waypoints[0].angle
npc2 = sim.add_agent('SUV', lgsvl.AgentType.NPC, state)
npc2.follow(smooth_waypoints,loop=True)

input("Press Enter to run")

sim.run() 