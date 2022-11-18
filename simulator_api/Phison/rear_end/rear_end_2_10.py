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

# EGO vehicle 抓取 Autoware 主機的 IP（環境變數：BRIDGE_HOST）和 Port號
a.connect_bridge(os.environ.get("BRIDGE_HOST", "192.168.0.171"),9090)
# a.connect_bridge(os.environ.get("BRIDGE_HOST", "192.168.0.147"),9090)

print("Waiting for connection...")
while not a.bridge_connected:
  time.sleep(1)
#印出是否連線成功
print("Bridge connected:", a.bridge_connected)

#NPC Vehicle
waypoints = [
  # lgsvl.DriveWaypoint(lgsvl.Vector(6805.8892, -63.1182, -8185.5781), 10, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  # lgsvl.DriveWaypoint(lgsvl.Vector(6806.5225, -63.1185, -8186.9507), 10, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  # lgsvl.DriveWaypoint(lgsvl.Vector(6807.0215, -63.1184, -8188.0366), 10, lgsvl.Vector(0, 153.6, 0), 0, True, 0), 
  # lgsvl.DriveWaypoint(lgsvl.Vector(6807.5254, -63.1184, -8189.1284), 10, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  # lgsvl.DriveWaypoint(lgsvl.Vector(6808.1592, -63.1186, -8190.5044), 10, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  # lgsvl.DriveWaypoint(lgsvl.Vector(6808.7056, -63.1186, -8191.6875), 10, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  # lgsvl.DriveWaypoint(lgsvl.Vector(6809.4136, -63.1187, -8193.2188), 10, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  # lgsvl.DriveWaypoint(lgsvl.Vector(6809.874, -63.1187, -8194.2139), 10, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  # lgsvl.DriveWaypoint(lgsvl.Vector(6810.4453, -63.1187, -8195.4492), 10, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  # lgsvl.DriveWaypoint(lgsvl.Vector(6810.9775, -63.1189, -8196.5967), 10, lgsvl.Vector(0, 153.6, 0), 0, True, 0), # 10
  lgsvl.DriveWaypoint(lgsvl.Vector(6811.7109, -63.1191, -8198.1885), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6812.3506, -63.1191, -8199.5752), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6812.856, -63.1191, -8200.6592), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6813.4385 ,-63.1191, -8201.9131), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6814.2666 ,-63.1192, -8203.7002), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6814.7656 ,-63.1192, -8204.7803), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6815.2646 ,-63.1192, -8205.8604), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6815.9419 ,-63.1192, -8207.3252), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6816.5786 ,-63.1192, -8208.6963), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0), # 20
  lgsvl.DriveWaypoint(lgsvl.Vector(6817.0708 ,-63.1192, -8209.7627), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6817.731 ,-63.1193, -8211.1885), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6818.2876 ,-63.1193, -8212.3896), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6818.9185 ,-63.1193, -8213.751), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6819.3975 ,-63.1193, -8214.79), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6820.0933 ,-63.1193, -8216.293), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6820.5327 ,-63.1193, -8217.2422), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6821.1919 ,-63.1193, -8218.666), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6822.0244 ,-63.1193, -8220.4668), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6822.6387 ,-63.1193, -8221.7949), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0), # 30
  lgsvl.DriveWaypoint(lgsvl.Vector(6823.541 ,-63.1192, -8223.7422), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6824.1826 ,-63.1192, -8225.1309), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6824.6816 ,-63.1192, -8226.2109), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6825.1094 ,-63.1192, -8227.1367), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6825.8198 ,-63.1192, -8228.667), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6826.3823 ,-63.1192, -8229.8857), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6827.2612 ,-63.1192, -8231.79), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6828.0317 ,-63.1192, -8233.4473), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6828.8639 ,-63.1192, -8235.252), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6829.3491 ,-63.1192, -8236.3047), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0), # 40
  lgsvl.DriveWaypoint(lgsvl.Vector(6829.7998 ,-63.1192, -8237.2705), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6830.2808 ,-63.1192, -8238.3096), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6831.0327 ,-63.1191, -8239.9424), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6831.6479 ,-63.1191, -8241.2705), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6832.1265 ,-63.1191, -8242.2959), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6832.6323 ,-63.1191, -8243.3945), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6833.2051 ,-63.1191, -8244.6396), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6833.8452 ,-63.1191, -8246.0186), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6834.3506 ,-63.1191, -8247.1025), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6834.9312 ,-63.1191, -8248.3193), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0), # 50
  lgsvl.DriveWaypoint(lgsvl.Vector(6835.6763 ,-63.1191, -8249.8877), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6836.5186 ,-63.1191, -8251.6699), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6837.0576 ,-63.1191, -8252.8008), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6837.6304 ,-63.1191, -8253.9961), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6838.0957 ,-63.1191, -8254.9805), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6838.6934 ,-63.119, -8256.2461), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6839.3906 ,-63.119, -8257.7051), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6840.3135 ,-63.119, -8259.6465), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6840.9351 ,-63.119, -8260.9629), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6841.5811 ,-63.119, -8262.877), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0), # 60
  lgsvl.DriveWaypoint(lgsvl.Vector(6842.3701 ,-63.119, -8263.9707), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6842.8857 ,-63.119, -8265.0645), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6843.3369 ,-63.119, -8266.0117), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6843.917 ,-63.119, -8267.2246), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6844.938 ,-63.119, -8269.3809), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6845.7314 ,-63.119, -8271.0459), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6846.2075 ,-63.119, -8272.042), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6846.7432 ,-63.119, -8273.1709), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6847.2432 ,-63.119, -8274.2324), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6847.8057 ,-63.1189, -8275.4102), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0), # 70
  lgsvl.DriveWaypoint(lgsvl.Vector(6848.4932 ,-63.1189, -8276.8496), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6849.0195 ,-63.1189, -8277.9619), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6849.4751 ,-63.1189, -8278.9268), 5, lgsvl.Vector(0, 153.6, 0), 0, True, 0),
]

state.transform = spawns[0]

state.transform.position.x =  6811.7109
state.transform.position.y =  -63.1191
state.transform.position.z =  -8198.1885
state.transform.rotation.y = 153.6

state.transform.position = waypoints[0].position
npc1 = sim.add_agent('Sedan', lgsvl.AgentType.NPC, state)


# 11.1 m/s is ~40 km/h , 5.6 m/s is ~20 km/h
#Activity NPC
# npc1.follow_closest_lane(True, 5.5)
npc1.follow(waypoints,loop=True)

def on_collision(agent1, agent2, contact):
  name1 = "STATIC OBSTACLE" if agent1 is None else agent1.name
  name2 = "STATIC OBSTACLE" if agent2 is None else agent2.name
  print("{} collided with {} at {}".format(name1, name2, contact))

a.on_collision(on_collision)
# npc1.on_collision(on_collision)


input("Press Enter to run")

sim.run() 
