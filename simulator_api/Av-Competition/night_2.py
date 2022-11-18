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
sim.weather = lgsvl.WeatherState(rain=0, fog=1, wetness=0)


state = lgsvl.AgentState()                                     #set the state of the car
state.transform.position = lgsvl.Vector(-29.59,0.04,-30.78)
state.transform.rotation.y = 159.29

state2 = lgsvl.AgentState()                                                   #set the state of the pedestrain 
state2.transform.position = lgsvl.Vector(-25.51,0.13,-44.93)
state2.transform.rotation.y = -19.86
npc = sim.add_agent("Presley", lgsvl.AgentType.PEDESTRIAN, state2)                     #generate the pedestrain 


ego = sim.add_agent("NCKU-Lincoln-MKZ", lgsvl.AgentType.EGO, state)           #generate the car 
ego.connect_bridge("140.116.245.163", 9090)

print("Waiting for connection...")

while not ego.bridge_connected:
  time.sleep(1)

print("Bridge connected:", ego.bridge_connected)



sim.run()

