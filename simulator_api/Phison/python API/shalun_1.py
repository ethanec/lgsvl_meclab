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
state.transform = spawns[0]
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
  lgsvl.DriveWaypoint(lgsvl.Vector(6777.826,-63.1182,-8187.86), 6, lgsvl.Vector(0, 153, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6780.38,-63.11819,-8192.879), 6, lgsvl.Vector(0, 153, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6783.709,-63.11819,-8199.343), 6, lgsvl.Vector(0, 153, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6788.025,-63.11819,-8208.006), 6, lgsvl.Vector(0, 153, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6792.319,-63.11819,-8217.584), 6, lgsvl.Vector(0, 160, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6796.115,-63.11819,-8225.942), 6, lgsvl.Vector(0, 165, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6796.386,-63.11819,-8229.043), 6, lgsvl.Vector(0, 170, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6797.06,-63.11819,-8233.67), 6, lgsvl.Vector(0, 170, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6798.521,-63.11819,-8238.63), 6, lgsvl.Vector(0, 160, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6801.033,-63.1182,-8245.638), 6, lgsvl.Vector(0, 170, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6799.717,-63.11819,-8251.112), 6, lgsvl.Vector(0, -160, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6794.966,-63.11819,-8254.498), 6, lgsvl.Vector(0, -120, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6790.648,-63.11819,-8254.944), 6, lgsvl.Vector(0, -60, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6785.702,-63.11819,-8253.016), 6, lgsvl.Vector(0, -30, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6783.876,-63.1182,-8248.954), 6, lgsvl.Vector(0, -25, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6782.064,-63.11819,-8245.328), 6, lgsvl.Vector(0, -25, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6780.026,-63.11819,-8241.249), 6, lgsvl.Vector(0, -25, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6776.717,-63.11819,-8234.626), 6, lgsvl.Vector(0, -25, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6772.752,-63.1182,-8226.688), 6, lgsvl.Vector(0, -25, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6769.377,-63.11819,-8219.934), 6, lgsvl.Vector(0, -25, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6766.313,-63.11819,-8213.802), 6, lgsvl.Vector(0, -25, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6762.549,-63.11819,-8206.064), 6, lgsvl.Vector(0, -25, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6760.435,-63.11819,-8200.5), 6, lgsvl.Vector(0, -10, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6758.598,-63.11819,-8193.361), 6, lgsvl.Vector(0, 5, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6759.147,-63.1182,-8189.606), 6, lgsvl.Vector(0, 30, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6763.378,-63.11819,-8186.841), 6, lgsvl.Vector(0, 60, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6767.066,-63.11819,-8185.606), 6, lgsvl.Vector(0, 80, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6774.239,-63.11819,-8186.08), 6, lgsvl.Vector(0, 120, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6776.988,-63.11819,-8188.242), 6, lgsvl.Vector(0, 140, 0), 0, True, 0),
]

def waypoint_minus(waypoint_a, waypoint_b, interval):
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
npc1.follow(waypoints,loop=True)


input("Press Enter to run")

sim.run() 
