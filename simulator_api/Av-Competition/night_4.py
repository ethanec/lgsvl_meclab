#!/usr/bin/env python3

import os
import lgsvl
import math
import time


sim = lgsvl.Simulator(os.environ.get("SIMULATOR_HOST", "127.0.0.1"), 8181)    #load shalun map
if sim.current_scene == "Shalun_night":
  sim.reset()
else:
  sim.load("Shalun_night")
sim.set_time_of_day(19)


state = lgsvl.AgentState()                                     #set the state of the car
state.transform.position = lgsvl.Vector(40.29,0.04,-4.46)
state.transform.rotation.y = 159.817


ego = sim.add_agent("NCKU-Lincoln-MKZ", lgsvl.AgentType.EGO, state)           #generate the car 

ego.connect_bridge("140.116.245.163", 9090)

print("Waiting for connection...")

while not ego.bridge_connected:
  time.sleep(1)

print("Bridge connected:", ego.bridge_connected)


sim.run()

