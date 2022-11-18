# -*- coding: utf-8 -*-
import os
import lgsvl
import time

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

#NPC Vehicle
waypoints = [
  lgsvl.DriveWaypoint(lgsvl.Vector(6799.459,-63.11819,-8181.093), 6, lgsvl.Vector(0, 151.88, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6805.212,-63.11819,-8192.79), 6, lgsvl.Vector(0, 153.952, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6813.232,-63.11819,-8210.998), 6, lgsvl.Vector(0, 154.998, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6813.946,-63.11819,-8212.17), 6, lgsvl.Vector(0, 150.732, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6814.481,-63.11819,-8212.975), 6, lgsvl.Vector(0, 147.99, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6815.238,-63.11819,-8213.851), 6, lgsvl.Vector(0, 141.922, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6815.87,-63.11819,-8214.584), 6, lgsvl.Vector(0, 140.052, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6816.305,-63.11819,-8215.092), 6, lgsvl.Vector(0, 140.051, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6817.073,-63.11819,-8216.22), 6, lgsvl.Vector(0, 144.817, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6817.749,-63.11819,-8217.123), 6, lgsvl.Vector(0, 144.817, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6818.454,-63.11819,-8218.286), 6, lgsvl.Vector(0, 147.012, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6819.411,-63.11819,-8220.237), 6, lgsvl.Vector(0, 152.983, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6820.531,-63.11819,-8222.604), 6, lgsvl.Vector(0, 154.647, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6820.994,-63.11819,-8223.584), 6, lgsvl.Vector(0, 155.086, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6824.38,-63.11819,-8230.851), 6, lgsvl.Vector(0, 155.086, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6826.782,-63.11819,-8236), 6, lgsvl.Vector(0, 155.087, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6831.487,-63.11819,-8246.138), 6, lgsvl.Vector(0, 155.089, 0), 0, True, 0),
]

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

  # print(temp.angle)
  smooth_waypoints.append(lgsvl.DriveWaypoint(lgsvl.Vector(x,y,z), 6, lgsvl.Vector(0, yaw, 0), 0, True, 0))

  for i in range(len(waypoints)-1):
    waypoint_vec = waypoint_minus(waypoints[i], waypoints[i+1], interval)

    for j in range(interval):
      x = x + waypoint_vec[0]
      y = y + waypoint_vec[1]
      z = z + waypoint_vec[2]
      yaw = yaw + waypoint_vec[3]
      # print(temp.angle)
      smooth_waypoints.append(lgsvl.DriveWaypoint(lgsvl.Vector(x,y,z), 6, lgsvl.Vector(0, yaw, 0), 0, True, 0))

  # for i in range(len(smooth_waypoints)):
  #   print(i, smooth_waypoints[i].angle)

  return smooth_waypoints

smooth_waypoints = smooth(waypoints, 5)

state.transform.position = smooth_waypoints[0].position
state.transform.rotation = smooth_waypoints[0].angle

npc1 = sim.add_agent('Motor', lgsvl.AgentType.NPC, state)

# 11.1 m/s is ~40 km/h , 5.6 m/s is ~20 km/h
#Activity NPC
# npc1.follow_closest_lane(True, 5.5)


npc1.follow(smooth_waypoints,loop=True)

input("Press Enter to run")

sim.run() 