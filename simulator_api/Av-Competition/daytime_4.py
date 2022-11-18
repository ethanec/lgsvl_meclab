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

speed =10.3
state = lgsvl.AgentState()                                     #set the state of the car
state.transform.position = lgsvl.Vector(-21.13,-0.02,14.41)
state.transform.rotation.y = -200.2

forward = lgsvl.utils.transform_to_forward(state.transform)                   #transform the axis velocity to forward velocity 

state.velocity = 8.4 * forward                                                #set velocity 
ego = sim.add_agent("NCKU-Lincoln-MKZ", lgsvl.AgentType.EGO, state)           #generate the car 

ego.connect_bridge("140.116.245.163", 9090)

print("Waiting for connection...")

while not ego.bridge_connected:
  time.sleep(1)

print("Bridge connected:", ego.bridge_connected)


state2 = lgsvl.AgentState()                                                   #set the state of the pedestrain 
state2.transform.position = lgsvl.Vector(-16.22,0.13,-9.74)
state2.transform.rotation.y = 71.78
npc = sim.add_agent("Bob", lgsvl.AgentType.PEDESTRIAN, state2)                     #generate the pedestrain 

waypoints = [
  lgsvl.WalkWaypoint(lgsvl.Vector(-16.22,0.13,-9.74), 0, 25),
  lgsvl.WalkWaypoint(lgsvl.Vector(-14.3,0.13,-9.11), 0, 0),
  lgsvl.WalkWaypoint(lgsvl.Vector(-8.82,0.13,-7.31), 0, 0),
  lgsvl.WalkWaypoint(lgsvl.Vector(-5.37,0.13,-6.18), 0, 0),
] 


npc.follow(waypoints)

sim.run()

