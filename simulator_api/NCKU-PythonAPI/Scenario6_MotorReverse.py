# -*- coding: utf-8 -*-
"""
@author: Chen-Xuan LIN
NCKU Intersection Sacenario
Sacenario : Motor drive on the wrong side of the road
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
state.transform.position = lgsvl.Vector( 454.5, 0.1, 421.7)
state.transform.rotation = lgsvl.Vector( 0, -175, 0)
ego = sim.add_agent("NCKU-Lincoln-MKZ", lgsvl.AgentType.EGO, state)

#Motor follow the waypoints
waypoints  = [ 
    lgsvl.DriveWaypoint(lgsvl.Vector( 441, 0, 325.5), 10, lgsvl.Vector(0, 0, 0), 0, False, 0),
    lgsvl.DriveWaypoint(lgsvl.Vector( 455.5, 0, 450), 10, lgsvl.Vector(0, 0, 0), 0, False, 0)
]
state.transform.position = waypoints[0].position
state.transform.rotation = lgsvl.Vector( 0, 9, 0)
NPC = sim.add_agent("Motor", lgsvl.AgentType.NPC, state)
NPC.follow(waypoints , loop=False)

input("Press Enter to run")
sim.run() 
