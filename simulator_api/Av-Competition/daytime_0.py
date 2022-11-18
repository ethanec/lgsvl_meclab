#!/usr/bin/env python3

import os
import lgsvl
import time

sim = lgsvl.Simulator(os.environ.get("SIMULATOR_HOST", "127.0.0.1"), 8181)    #load shalun map
if sim.current_scene == "Shalun_daytime":
  sim.reset()
else:
  sim.load("Shalun_daytime")

state = lgsvl.AgentState() 
state.transform.position = lgsvl.Vector(-13.72,0.11,75.98)
state.transform.rotation.x = 3.222286e-41
state.transform.rotation.y = -200.08


ego = sim.add_agent("NCKU-Lincoln-MKZ", lgsvl.AgentType.EGO, state)           #generate the car 

ego.connect_bridge("140.116.245.163", 9090)

print("Waiting for connection...")

while not ego.bridge_connected:
  time.sleep(1)

print("Bridge connected:", ego.bridge_connected)



sim.run()