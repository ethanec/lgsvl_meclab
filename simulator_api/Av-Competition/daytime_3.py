#!/usr/bin/env python3

import os
import lgsvl
import math
import time

sim = lgsvl.Simulator(os.environ.get("SIMULATOR_HOST", "127.0.0.1"), 8181)    #load shalun map
if sim.current_scene == "Shalun_daytime":
  sim.reset()
else:
  sim.load("Shalun_daytime")


state = lgsvl.AgentState()                                     #set the state of the car
state.transform.position = lgsvl.Vector(21.99,0.04,-2.52)
state.transform.rotation.y = -19.72

forward = lgsvl.utils.transform_to_forward(state.transform)                   #transform the axis velocity to forward velocity 

state.velocity = 8.4 * forward                                                #set velocity 
ego = sim.add_agent("NCKU-Lincoln-MKZ", lgsvl.AgentType.EGO, state)           #generate the car 

ego.connect_bridge("140.116.245.163", 9090)

print("Waiting for connection...")

while not ego.bridge_connected:
  time.sleep(1)

print("Bridge connected:", ego.bridge_connected)


state2 = lgsvl.AgentState()                                                   #set the state of the motorbike 
state2.transform.position = lgsvl.Vector(19.85,0.082,12.06)
state2.transform.rotation.y = -22.9
npc = sim.add_agent("Motor", lgsvl.AgentType.NPC, state2)                     #generate the motorbike 



waypoints = [
  lgsvl.DriveWaypoint(lgsvl.Vector(19.85,0.082,12.06), 3, lgsvl.Vector(0, 0, 0), 0, False, 10),
  lgsvl.DriveWaypoint(lgsvl.Vector(16.16,0.082,15.1), 4, lgsvl.Vector(0, 0, 0), 0, False, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(11.61,0.082,24.16), 6, lgsvl.Vector(0, 0, 0), 0, False, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6.68,0.082,37.46), 7, lgsvl.Vector(0, 0, 0), 0, False, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(4.54,0.08,44.14), 7, lgsvl.Vector(0, 0, 0), 0, False, 0),
]


npc.follow(waypoints)

sim.run()

