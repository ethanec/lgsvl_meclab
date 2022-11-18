# -*- coding: utf-8 -*-
"""
@author: Chen-Xuan LIN
NCKU Intersection Sacenario
Sacenario : Motor and ego car go straight in Intersection
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
state.transform = spawns[1]
a = sim.add_agent("NCKU-Lincoln-MKZ", lgsvl.AgentType.EGO, state)

right = lgsvl.utils.transform_to_right(spawns[1])
forward = lgsvl.utils.transform_to_forward(spawns[1])
#NPC Vehicle , spawn for spwans[1] 

#右側機車

state.transform.position = spawns[1].position + right * 2 + forward
npc1 = sim.add_agent('Motor', lgsvl.AgentType.NPC, state)
state.transform.position = spawns[1].position + right * 1 - forward
npc2 = sim.add_agent('Motor', lgsvl.AgentType.NPC, state)
state.transform.position = spawns[1].position + right * 1 + forward
npc3 = sim.add_agent('Motor', lgsvl.AgentType.NPC, state)
state.transform.position = spawns[1].position - forward * 2
npc4 = sim.add_agent('Motor', lgsvl.AgentType.NPC, state) 
state.transform.position = spawns[1].position - right - forward
npc5 = sim.add_agent('Motor', lgsvl.AgentType.NPC, state)
state.transform.position = spawns[1].position - right + forward
npc6 = sim.add_agent('Motor', lgsvl.AgentType.NPC, state)


# 11.1 m/s is ~40 km/h , 5.6 m/s is ~20 km/h
#Activity NPC
npc1.follow_closest_lane(True, 5.6)
npc2.follow_closest_lane(True, 5.6)
npc3.follow_closest_lane(True, 5.6)
npc4.follow_closest_lane(True, 5.6)
npc5.follow_closest_lane(True, 5.6)
npc6.follow_closest_lane(True, 5.6)
input("Press Enter to run")

sim.run() 
