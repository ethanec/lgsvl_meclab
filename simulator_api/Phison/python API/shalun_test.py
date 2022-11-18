#!/usr/bin/env python3
#
# Copyright (c) 2019 LG Electronics, Inc.
#
# This software contains code licensed as described in LICENSE.
#

import os
import lgsvl
import collections
import time
import random
# 抓取模擬器主機的 IP（環境變數：SIMULATOR_HOST）和 Port號
sim = lgsvl.Simulator(os.environ.get("SIMULATOR_HOST","127.0.0.1"), 8181)
#設定場景
if sim.current_scene == "Shalun_NCKU":
  sim.reset()
else:
  sim.load("Shalun_NCKU")
#NPC名子種類 
NPCname = [
    'Sedan',
    'HatchBack'
]
#設定waypoint座標與車輛速度
waypoints = [
  lgsvl.DriveWaypoint(lgsvl.Vector(-85,10.2,-7.32), 12),
  lgsvl.DriveWaypoint(lgsvl.Vector(-85.42,10.2,2.51), 12),
  lgsvl.DriveWaypoint(lgsvl.Vector(-85.42,10.2,5.97), 12),
  lgsvl.DriveWaypoint(lgsvl.Vector(-80,10.2,11), 12),
  lgsvl.DriveWaypoint(lgsvl.Vector(-50,10.2,11), 12),
  lgsvl.DriveWaypoint(lgsvl.Vector(-30,10.2,11), 12),
  lgsvl.DriveWaypoint(lgsvl.Vector( 0 ,10.2,11), 12),
  lgsvl.DriveWaypoint(lgsvl.Vector( 20 ,10.2,11), 12),
  lgsvl.DriveWaypoint(lgsvl.Vector( 53,10.2,11), 12),
  lgsvl.DriveWaypoint(lgsvl.Vector( 55.93,10.2,10), 12),
  lgsvl.DriveWaypoint(lgsvl.Vector( 58.34,10.2,8.82), 12),
  lgsvl.DriveWaypoint(lgsvl.Vector( 59 ,10.2,6.92), 12),
  lgsvl.DriveWaypoint(lgsvl.Vector( 60,10.2,-27), 12),
  lgsvl.DriveWaypoint(lgsvl.Vector( 59.46, 10.2,-29.1), 12),
  lgsvl.DriveWaypoint(lgsvl.Vector( 57.54, 10.2,-32), 12),
  lgsvl.DriveWaypoint(lgsvl.Vector( 55   , 10.2,-33.43), 12),
  lgsvl.DriveWaypoint(lgsvl.Vector( 20, 10.2,-33), 12),
  lgsvl.DriveWaypoint(lgsvl.Vector( 0, 10.2,-33), 12),
  lgsvl.DriveWaypoint(lgsvl.Vector( -30, 10.2,-33), 12),
  lgsvl.DriveWaypoint(lgsvl.Vector( -67, 10.2,-33), 12),
  lgsvl.DriveWaypoint(lgsvl.Vector( -71.32, 10.2,-31.95), 12),
  lgsvl.DriveWaypoint(lgsvl.Vector( -73.88, 10.2,-30.59), 12),
  lgsvl.DriveWaypoint(lgsvl.Vector( -76.51, 10.2,-28.9), 12),
  lgsvl.DriveWaypoint(lgsvl.Vector( -79.13, 10.2,-26.3), 12),
  lgsvl.DriveWaypoint(lgsvl.Vector( -82.2,10.2,-21.5), 12),
  lgsvl.DriveWaypoint(lgsvl.Vector( -83.95,10.2,-16.5), 12),
]

#設定 EGO 起始位置 
spawns = sim.get_spawn()
state = lgsvl.AgentState()
state.transform = spawns[0]
state.transform.position.x =  6769.801
state.transform.position.y =  -63.11819
state.transform.position.z =  -8162.083
state.transform.rotation.y = 154.54
#加入 EGO  , add_agent(名稱,類別,位置)
ego = sim.add_agent("NCKU-Lincoln-MKZ", lgsvl.AgentType.EGO, state)

# EGO vehicle 抓取 Autoware 主機的 IP（環境變數：BRIDGE_HOST）和 Port號
ego.connect_bridge(os.environ.get("BRIDGE_HOST", "127.0.0.1"),8080)
print("Waiting for connection...")
while not ego.bridge_connected:
  time.sleep(1)
#印出是否連線成功
print("Bridge connected:", ego.bridge_connected)


#設定 NPC 起始位置
state = lgsvl.AgentState()
state.transform = spawns[0]
state.transform.position.x = -48.67
state.transform.position.y =  10.2
state.transform.position.z =  15
state.transform.rotation.y = -90
npc0 = sim.add_agent(random.choice(NPCname), lgsvl.AgentType.NPC, state)

state.transform.rotation.y =  0
state.transform.position = waypoints[0].position
npc1 = sim.add_agent(random.choice(NPCname), lgsvl.AgentType.NPC, state)
#NPC.follow(waypoint,是否重複依循waypoint)
npc1.follow(waypoints,True)

#Change waypoints index for  NPC2 
waypoints.insert(0,waypoints.pop())
waypoints.insert(0,waypoints.pop())
state.transform.position = waypoints[0].position
npc2 = sim.add_agent(random.choice(NPCname), lgsvl.AgentType.NPC, state)
npc2.follow(waypoints,True)

#Change waypoints index for  NPC3
waypoints.insert(0,waypoints.pop())
waypoints.insert(0,waypoints.pop())
waypoints.insert(0,waypoints.pop())
waypoints.insert(0,waypoints.pop())
state.transform.rotation.y = -21
state.transform.position = waypoints[0].position
npc3 = sim.add_agent(random.choice(NPCname), lgsvl.AgentType.NPC, state)
npc3.follow(waypoints,True)

#Change waypoints index for  NPC4
waypoints.insert(0,waypoints.pop())
waypoints.insert(0,waypoints.pop())
state.transform.rotation.y = -75
state.transform.position = waypoints[-2].position
npc4 = sim.add_agent(random.choice(NPCname), lgsvl.AgentType.NPC, state)
npc4.follow(waypoints,True)

input("Press Enter to run")
#開始執行Simulator
sim.run()
