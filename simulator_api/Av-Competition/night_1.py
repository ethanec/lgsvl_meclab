#!/usr/bin/env python3

import os
import lgsvl
import time


sim = lgsvl.Simulator(os.environ.get("SIMULATOR_HOST", "127.0.0.1"), 8181)    #load shalun map
if sim.current_scene == "Shalun_night":
  sim.reset()
else:
  sim.load("Shalun_night")

state = lgsvl.AgentState() 
state.transform.position = lgsvl.Vector(12.58,0.11,-14)
state.transform.rotation.x = -0.241
state.transform.rotation.y = 159.92


ego = sim.add_agent("NCKU-Lincoln-MKZ", lgsvl.AgentType.EGO, state)           #generate the car 

sim.set_time_of_day(19)   #night scenario

ego.connect_bridge("140.116.245.163", 9090)

print("Waiting for connection...")

while not ego.bridge_connected:
  time.sleep(1)

print("Bridge connected:", ego.bridge_connected)


sim.run()