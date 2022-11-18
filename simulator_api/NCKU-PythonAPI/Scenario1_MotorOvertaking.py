# -*- coding: utf-8 -*-
"""
@author: Chen-Xuan LIN
NCKU MotorOvertaking Sacenario

Before start this scenario , make sure ego car has motorOvertake-scrip
Sacenario : Motor overtake
"""
import os
import lgsvl

#Load Map
sim = lgsvl.Simulator(os.environ.get("SIMULATOR_HOST", "127.0.0.1"), 8181)
if sim.current_scene == "Highway86":
  sim.reset()
else:
  sim.load("Highway86")
spawns = sim.get_spawn()
sim.set_time_of_day(9.5)

#Ego Vehicle
state = lgsvl.AgentState()
state.transform = spawns[0]
a = sim.add_agent("NCKU-Lincoln-MKZ", lgsvl.AgentType.EGO, state)


#NPC Vehicle , spawn for spwans[0] 
state.transform.position = spawns[0].position + lgsvl.Vector(-1,0,15)

npc1 = sim.add_agent('Motor', lgsvl.AgentType.NPC, state)


# 11.1 m/s is ~40 km/h , 5.6 m/s is ~20 km/h
#Activity NPC
npc1.follow_closest_lane(True, 16.8)

input("Press Enter to run")

sim.run() 
