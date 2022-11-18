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
  lgsvl.DriveWaypoint(lgsvl.Vector(6801.858,-63.11819,-8184.887), 6, lgsvl.Vector(0, 154.575, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6804.443,-63.11819,-8190.268), 6, lgsvl.Vector(0, 154.577, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6809.979,-63.11819,-8201.917), 6, lgsvl.Vector(0, 154.576, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6812.952,-63.11819,-8207.934), 6, lgsvl.Vector(0, 153.038, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6813.87,-63.11819,-8209.207), 6, lgsvl.Vector(0, 146.912, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6815.837,-63.11819,-8211.748), 6, lgsvl.Vector(0, 141.649, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6817.165,-63.11819,-8213.432), 6, lgsvl.Vector(0, 141.417, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6819.555,-63.11819,-8216.436), 6, lgsvl.Vector(0, 141.417, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6820.808,-63.11819,-8218.254), 6, lgsvl.Vector(0, 145.891, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6821.505,-63.11819,-8219.513), 6, lgsvl.Vector(0, 149.68, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6822.041,-63.11819,-8220.575), 6, lgsvl.Vector(0, 152.123, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6825.963,-63.11819,-8228.361), 6, lgsvl.Vector(0, 154.084, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6833.435,-63.11819,-8244.241), 6, lgsvl.Vector(0, 155.23, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6834.219,-63.11819,-8246.33), 6, lgsvl.Vector(0, 159.345, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6834.46,-63.11819,-8247.449), 6, lgsvl.Vector(0, 164.422, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6834.507,-63.11819,-8248.524), 6, lgsvl.Vector(0, 172.432, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6834.55,-63.11819,-8250.912), 6, lgsvl.Vector(0, 177.662, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6834.62,-63.11819,-8252.554), 6, lgsvl.Vector(0, 177.663, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6834.972,-63.11819,-8254.82), 6, lgsvl.Vector(0, 170.616, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6835.247,-63.11819,-8255.695), 6, lgsvl.Vector(0, 166.439, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6835.648,-63.11819,-8256.697), 6, lgsvl.Vector(0, 161.371, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6836.035,-63.11819,-8257.516), 6, lgsvl.Vector(0, 158.036, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6836.329,-63.11819,-8258.132), 6, lgsvl.Vector(0, 157.152, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6838.574,-63.11819,-8262.981), 6, lgsvl.Vector(0, 154.843, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6841,-63.11819,-8268.131), 6, lgsvl.Vector(0, 154.844, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6846.837,-63.11819,-8280.561), 6, lgsvl.Vector(0, 154.846, 0), 0, True, 0),
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