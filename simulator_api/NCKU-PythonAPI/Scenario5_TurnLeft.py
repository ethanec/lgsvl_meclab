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
state.transform.position = lgsvl.Vector( 405.8, 0.1, 169.4)
state.transform.rotation = lgsvl.Vector( 0, -159.3, 0)
ego = sim.add_agent("NCKU-Lincoln-MKZ", lgsvl.AgentType.EGO, state)



#Motor follow the waypoints in the opposite direction
waypoints  = [ 
    lgsvl.DriveWaypoint(lgsvl.Vector( 391.1, 0.1, 101.7), 0, lgsvl.Vector(0, 0, 0), 0, True, 65),
    lgsvl.DriveWaypoint(lgsvl.Vector( 414.7, 0.1, 160.8), 10, lgsvl.Vector(0, 22, 0), 0, False, 0)
]
state.transform.position = waypoints[0].position
state.transform.rotation = lgsvl.Vector( 0, 384.6, 0)
NPC4 = sim.add_agent("Motor", lgsvl.AgentType.NPC, state)
NPC4.follow(waypoints , loop=False)

waypoints  = [ 
    lgsvl.DriveWaypoint(lgsvl.Vector( 394.3, 0.1, 105.4), 0, lgsvl.Vector(0, 0, 0), 0, True, 65),
    lgsvl.DriveWaypoint(lgsvl.Vector( 416.2, 0.1, 160.1), 5, lgsvl.Vector(0, 21.2, 0), 0, False, 0)
]
state.transform.position = waypoints[0].position
state.transform.rotation = lgsvl.Vector( 0, 384.6, 0)
NPC5 = sim.add_agent("Motor", lgsvl.AgentType.NPC, state)
NPC5.follow(waypoints , loop=False)

waypoints  = [ 
    lgsvl.DriveWaypoint(lgsvl.Vector( 397.4, 0.1, 107.5), 0, lgsvl.Vector(0, 0, 0), 0, True, 60),
    lgsvl.DriveWaypoint(lgsvl.Vector( 417.8, 0.1, 159.3), 5, lgsvl.Vector(0, 22.9, 0), 0, False, 0)
]
state.transform.position = waypoints[0].position
state.transform.rotation = lgsvl.Vector( 0, 384.6, 0)
NPC6 = sim.add_agent("Motor", lgsvl.AgentType.NPC, state)
NPC6.follow(waypoints , loop=False)

input("Press Enter to run")
sim.run() 
