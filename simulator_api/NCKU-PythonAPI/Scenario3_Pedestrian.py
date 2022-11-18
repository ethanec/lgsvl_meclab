# -*- coding: utf-8 -*-
"""
@author: Chen-Xuan LIN
NCKU Intersection Sacenario
Sacenario : Interaction of vehicle and pedestrian in highway86
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
state.transform.position = lgsvl.Vector( 413, 0.1, 197)
state.transform.rotation = lgsvl.Vector( 0, 203, 0)
ego = sim.add_agent("NCKU-Lincoln-MKZ", lgsvl.AgentType.EGO, state)

#Pedestrian follow the waypoint 
wp = [ 
    lgsvl.WalkWaypoint( lgsvl.Vector(386, 0, 158), 0, 0), 
    lgsvl.WalkWaypoint( lgsvl.Vector(417, 0, 150), 0, 0)
]
state = lgsvl.AgentState()
state.transform.position = wp[0].position
ped = sim.add_agent("Pamela", lgsvl.AgentType.PEDESTRIAN, state)
state.transform.position = wp[0].position + lgsvl.Vector( 0.5, 0, 1)
ped1 = sim.add_agent("Bob", lgsvl.AgentType.PEDESTRIAN, state)
state.transform.position = wp[0].position + lgsvl.Vector( 2, 0, 1.5)
ped2 = sim.add_agent("Zoe", lgsvl.AgentType.PEDESTRIAN, state)

ped.follow(wp, True)
ped1.follow(wp, True)
ped2.follow(wp, True)

input("Press Enter to run")
sim.run() 

