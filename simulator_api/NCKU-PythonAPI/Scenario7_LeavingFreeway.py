# -*- coding: utf-8 -*-
"""
@author: Chen-Xuan LIN
NCKU Intersection Sacenario
Sacenario : Vehicle leaving freeway and go to surface street 
"""
import os
import lgsvl
import random
#Load Map
sim = lgsvl.Simulator(os.environ.get("SIMULATOR_HOST", "127.0.0.1"), 8181)
if sim.current_scene == "Highway86":
  sim.reset()
else:
  sim.load("Highway86")
sim.set_time_of_day(15)

#Ego Vehicle
state = lgsvl.AgentState()
state.transform.position = lgsvl.Vector( 416.6, 4.7, 676.8)
state.transform.rotation = lgsvl.Vector( 0, 125.4, 0)
ego = sim.add_agent("NCKU-Lincoln-MKZ", lgsvl.AgentType.EGO, state)


#Motor follow the lanes
MotoList = []

state.transform.position = lgsvl.Vector( 462.5, 0.1, 566.6)
state.transform.rotation = lgsvl.Vector( 0, -178.8, 0)
MotoList.append(sim.add_agent("Motor", lgsvl.AgentType.NPC, state))

state.transform.position = lgsvl.Vector( 460.8, 0.1, 560.8)
state.transform.rotation = lgsvl.Vector( 0, -178.8, 0)
MotoList.append(sim.add_agent("Motor", lgsvl.AgentType.NPC, state))

state.transform.position = lgsvl.Vector( 462.4, 0.1, 577)
state.transform.rotation = lgsvl.Vector( 0, -181.3, 0)
MotoList.append(sim.add_agent("Motor", lgsvl.AgentType.NPC, state))

state.transform.position = lgsvl.Vector( 460.8, 0.1, 573.8)
state.transform.rotation = lgsvl.Vector( 0, -181.2, 0)
MotoList.append(sim.add_agent("Motor", lgsvl.AgentType.NPC, state))

state.transform.position = lgsvl.Vector( 460.31, 0.1, 583.6)
state.transform.rotation = lgsvl.Vector( 0, -181.2, 0)
MotoList.append(sim.add_agent("Motor", lgsvl.AgentType.NPC, state))

state.transform.position = lgsvl.Vector( 462.0, 0.1, 586.4)
state.transform.rotation = lgsvl.Vector( 0, -181.2, 0)
MotoList.append(sim.add_agent("Motor", lgsvl.AgentType.NPC, state))

state.transform.position = lgsvl.Vector( 460.1, 0.1, 588.2)
state.transform.rotation = lgsvl.Vector( 0, -181.2, 0)
MotoList.append(sim.add_agent("Motor", lgsvl.AgentType.NPC, state))

for Moto in MotoList:
  Moto.follow_closest_lane(True, 6)



#Motor follow the waypoints
waypoints  = [
    lgsvl.DriveWaypoint(lgsvl.Vector( 453.0, 0, 622.9), 8, lgsvl.Vector(0, -178, 0), 0, False, 0),
    lgsvl.DriveWaypoint(lgsvl.Vector( 460.4, 0, 593.8), 8, lgsvl.Vector(0, -178, 0), 0, False, 0),
    lgsvl.DriveWaypoint(lgsvl.Vector( 463.7, 0, 512.4), 10, lgsvl.Vector(0, -178, 0), 0, False, 0),
    lgsvl.DriveWaypoint(lgsvl.Vector( 463.3, 0, 507.3), 10, lgsvl.Vector(0, -178, 0), 0, False, 0),
    lgsvl.DriveWaypoint(lgsvl.Vector( 463.7, 0, 503.2), 14, lgsvl.Vector(0, -178, 0), 0, False, 0),
    lgsvl.DriveWaypoint(lgsvl.Vector( 464.2, 0, 498.7), 14, lgsvl.Vector(0, -178, 0), 0, False, 0),
    lgsvl.DriveWaypoint(lgsvl.Vector( 437.8, 0, 289), 14, lgsvl.Vector(0, -178, 0), 0, False, 0)
]
state.transform.position = waypoints[0].position
state.transform.rotation = lgsvl.Vector( 0, -178, 0)

NPC7 = sim.add_agent("Motor", lgsvl.AgentType.NPC, state)
NPC7.follow(waypoints , loop=False)


input("Press Enter to run")
sim.run() 

