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
  lgsvl.DriveWaypoint(lgsvl.Vector(6842.859,-63.11819,-8247.9), 6, lgsvl.Vector(0, -25,0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6835.871,-63.11819,-8232.958), 6, lgsvl.Vector(0, -25, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6835.224,-63.11819,-8231.885), 6, lgsvl.Vector(0, -29.5, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6834.699,-63.11819,-8231.112), 6, lgsvl.Vector(0, -32.15, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6833.385,-63.11819,-8229.223), 6, lgsvl.Vector(0, -35, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6832.28,-63.11819,-8227.834), 6, lgsvl.Vector(0, -38.5, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6831.443,-63.11819,-8226.969), 6, lgsvl.Vector(0, -42.2, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6830.509,-63.11819,-8226.063), 6, lgsvl.Vector(0, -44.5, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6829.929,-63.11819,-8225.508), 6, lgsvl.Vector(0, -45.5, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6828.061,-63.11819,-8223.419), 6, lgsvl.Vector(0, -42.5, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6827.523,-63.11819,-8222.448), 6, lgsvl.Vector(0, -34.3, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6826.867,-63.11819,-8221.316), 6, lgsvl.Vector(0, -30.7, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6825.629,-63.11819,-8219.112), 6, lgsvl.Vector(0, -28.85, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6824.544,-63.11819,-8216.871), 6, lgsvl.Vector(0, -25.3, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6823.069,-63.11819,-8213.768), 6, lgsvl.Vector(0, -25.3, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6820.808,-63.11819,-8209.009), 6, lgsvl.Vector(0, -25.3, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6819.276,-63.11819,-8206.387), 6, lgsvl.Vector(0, -31.6, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6817.377,-63.11819,-8203.891), 6, lgsvl.Vector(0, -39.85, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6815.352,-63.11819,-8201.981), 6, lgsvl.Vector(0, -48.5, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6811.935,-63.11819,-8200.063), 6, lgsvl.Vector(0, -67.6, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6810.553,-63.11819,-8200.028), 6, lgsvl.Vector(0, -81.5, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6808.673,-63.11819,-8200.177), 6, lgsvl.Vector(0, -92.6, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6805.584,-63.11819,-8200.628), 6, lgsvl.Vector(0, -99.7, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6804.427,-63.11819,-8201.069), 6, lgsvl.Vector(0, -107, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6803.347,-63.11819,-8201.584), 6, lgsvl.Vector(0, -112, 0), 0, True, 0),
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