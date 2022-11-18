# -*- coding: utf-8 -*-
"""
@author: Chen-Xuan LIN
NCKU Intersection Sacenario
Sacenario : Motor and ego car trun right
"""
import os
import lgsvl

#Load Map
sim = lgsvl.Simulator(os.environ.get("SIMULATOR_HOST", "127.0.0.1"), 8181)
if sim.current_scene == "Highway86":
  sim.reset()
else:
  sim.load("Highway86")
sim.set_time_of_day(9.5)

#Ego Vehicle
state = lgsvl.AgentState()
state.transform.position = lgsvl.Vector( 396.8, 0.1, 164.1)
state.transform.rotation = lgsvl.Vector( 0, -157.4, 0)
ego = sim.add_agent("NCKU-Lincoln-MKZ", lgsvl.AgentType.EGO, state)

#Motor follow the lanes
state.transform.position = lgsvl.Vector( 396.5, 0.1, 171.8)
state.transform.rotation = lgsvl.Vector( 0, -157.4, 0)
NPC = sim.add_agent("Motor", lgsvl.AgentType.NPC, state)
state.transform.position = lgsvl.Vector( 395, 0.1, 165.5)
state.transform.rotation = lgsvl.Vector( 0, -157.4, 0)
NPC2 = sim.add_agent("Motor", lgsvl.AgentType.NPC, state)
state.transform.position = lgsvl.Vector( 402.2, 0.1, 183.4)
state.transform.rotation = lgsvl.Vector( 0, -157.4, 0)
NPC3 = sim.add_agent("Motor", lgsvl.AgentType.NPC, state)
state.transform.position = lgsvl.Vector( 400, 0.1, 180)
state.transform.rotation = lgsvl.Vector( 0, -157.4, 0)
NPC4 = sim.add_agent("Motor", lgsvl.AgentType.NPC, state)

NPC.follow_closest_lane(True, 11.2)
NPC2.follow_closest_lane(True, 5.6)
NPC3.follow_closest_lane(True, 5.6)
NPC4.follow_closest_lane(True, 5.6)

input("Press Enter to run")
sim.run() 
