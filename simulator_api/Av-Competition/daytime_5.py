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
state.transform.position = lgsvl.Vector(28.94,0.04,32.78)
state.transform.rotation.y = 159.8


ego = sim.add_agent("NCKU-Lincoln-MKZ", lgsvl.AgentType.EGO, state)           #generate the car 

ego.connect_bridge("140.116.245.163", 9090)

print("Waiting for connection...")

while not ego.bridge_connected:
  time.sleep(1)

print("Bridge connected:", ego.bridge_connected)


sim.run()

