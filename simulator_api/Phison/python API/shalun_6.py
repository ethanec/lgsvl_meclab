# -*- coding: utf-8 -*-

import os
import lgsvl
import time

#Load Map
sim = lgsvl.Simulator(os.environ.get("SIMULATOR_HOST", "127.0.0.1"), 8181)
if sim.current_scene == "shalun_moving_map_v2":
  sim.reset()
else:
  sim.load("shalun_moving_map_v2")
spawns = sim.get_spawn()
# sim.set_time_of_day(9.5)

#Ego Vehicle
state = lgsvl.AgentState()

state.transform.position.x =  6769.801
state.transform.position.y =  -63.11819
state.transform.position.z =  -8162.083
state.transform.rotation.y = 154.54

a = sim.add_agent("NCKU-Lincoln-MKZ", lgsvl.AgentType.EGO, state)

# # EGO vehicle 抓取 Autoware 主機的 IP（環境變數：BRIDGE_HOST）和 Port號
# a.connect_bridge(os.environ.get("BRIDGE_HOST", "192.168.0.147"),9090)
# print("Waiting for connection...")
# while not a.bridge_connected:
#   time.sleep(1)
# #印出是否連線成功
# print("Bridge connected:", a.bridge_connected)

#NPC Vehicle
waypoints = [
  lgsvl.DriveWaypoint(lgsvl.Vector(6803.573,-63.11819,-8181.294), 6, lgsvl.Vector(0, 153.517, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6806.148,-63.11819,-8186.567), 6, lgsvl.Vector(0, 153.857, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6815.341,-63.11819,-8205.84), 6, lgsvl.Vector(0, 155.101, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6816.777,-63.11819,-8209.869), 6, lgsvl.Vector(0, 160.279, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6816.997,-63.11819,-8211.065), 6, lgsvl.Vector(0, 166.16, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6817.146,-63.11819,-8213.068), 6, lgsvl.Vector(0, 175.072, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6817.496,-63.11819,-8216.863), 6, lgsvl.Vector(0, 175.073, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6817.692,-63.11819,-8218.288), 6, lgsvl.Vector(0, 172.482, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6818.261,-63.11819,-8220.528), 6, lgsvl.Vector(0, 165.171, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6818.886,-63.11819,-8221.556), 6, lgsvl.Vector(0, 155.858, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6821.545,-63.11819,-8227.471), 6, lgsvl.Vector(0, 155.858, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6832.926,-63.11819,-8251.538), 6, lgsvl.Vector(0, 155.247, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6842.664,-63.11819,-8271.66), 6, lgsvl.Vector(0, 154.219, 0), 0, True, 0),
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

npc1 = sim.add_agent('SUV', lgsvl.AgentType.NPC, state)

# 11.1 m/s is ~40 km/h , 5.6 m/s is ~20 km/h
#Activity NPC
# npc1.follow_closest_lane(True, 5.5)


npc1.follow(smooth_waypoints,loop=True)

input("Press Enter to run")

sim.run() 