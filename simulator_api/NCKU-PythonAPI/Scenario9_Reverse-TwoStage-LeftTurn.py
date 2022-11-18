# -*- coding: utf-8 -*-
"""
@author: Chen-Xuan LIN
NCKU Intersection Sacenario
Sacenario : Motorcycle turns left illegally
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
sim.set_time_of_day(9.5)

#Ego Vehicle
state = lgsvl.AgentState()
state.transform.position = lgsvl.Vector( 396.8, 0.1, 164.1)
state.transform.rotation = lgsvl.Vector( 0, -157.4, 0)
ego = sim.add_agent("NCKU-Lincoln-MKZ", lgsvl.AgentType.EGO, state)

#Ped setting
PedList = []
names = ["Bob", "EntrepreneurFemale", "Howard", "Johny", "Pamela", "Presley", "Robin", "Stephen", "Zoe"]

state = lgsvl.AgentState()
state.transform.position = lgsvl.Vector(386, 0, 158)
ped = sim.add_agent(random.choice(names), lgsvl.AgentType.PEDESTRIAN, state)
PedList.append(ped)
state.transform.position = lgsvl.Vector(371, 0, 162)
ped1 = sim.add_agent(random.choice(names), lgsvl.AgentType.PEDESTRIAN, state)
state.transform.position = lgsvl.Vector(394, 0, 180)
PedList.append(ped1)
ped2 = sim.add_agent(random.choice(names), lgsvl.AgentType.PEDESTRIAN, state)
state.transform.position = lgsvl.Vector(371, 0, 129)
PedList.append(ped2)
ped3 = sim.add_agent(random.choice(names), lgsvl.AgentType.PEDESTRIAN, state)
state.transform.position = lgsvl.Vector(415, 0, 128)
PedList.append(ped3)
ped4 = sim.add_agent(random.choice(names), lgsvl.AgentType.PEDESTRIAN, state)
state.transform.position = lgsvl.Vector(408, 0, 122)
PedList.append(ped4)
ped5 = sim.add_agent(random.choice(names), lgsvl.AgentType.PEDESTRIAN, state)
state.transform.position = lgsvl.Vector(363, 0, 150)
PedList.append(ped5)
ped6 = sim.add_agent(random.choice(names), lgsvl.AgentType.PEDESTRIAN, state)
state.transform.position = lgsvl.Vector(376, 0, 144)
PedList.append(ped6)
ped7 = sim.add_agent(random.choice(names), lgsvl.AgentType.PEDESTRIAN, state)
state.transform.position = lgsvl.Vector(371, 0, 146)
ped8 = sim.add_agent(random.choice(names), lgsvl.AgentType.PEDESTRIAN, state)
PedList.append(ped7)

for ped in PedList:
  ped.walk_randomly(True)

#Motor follow the lanes
state.transform.position = lgsvl.Vector( 394.15, 0.1, 163.16)
state.transform.rotation = lgsvl.Vector( 0, -157.4, 0)
NPC = sim.add_agent("Motor", lgsvl.AgentType.NPC, state)
state.transform.position = lgsvl.Vector( 393.56, 0.1, 164.02)
state.transform.rotation = lgsvl.Vector( 0, -157.4, 0)
NPC2 = sim.add_agent("Motor", lgsvl.AgentType.NPC, state)

NPC.follow_closest_lane(True, 11.2)
NPC2.follow_closest_lane(True, 5.6)


#Motor follow the waypoints
waypoints  = [
    lgsvl.DriveWaypoint(lgsvl.Vector( 387.2, 0, 88.7), 5, lgsvl.Vector(0, 0, 0), 0, False, 0),
    lgsvl.DriveWaypoint(lgsvl.Vector( 400, 0, 119), 5, lgsvl.Vector(0, 24, 0), 0, False, 0),
    lgsvl.DriveWaypoint(lgsvl.Vector( 400, 0, 119), 5, lgsvl.Vector(0, 24, 0), 0, False, 0),
    lgsvl.DriveWaypoint(lgsvl.Vector( 402.5, 0, 125.6), 5, lgsvl.Vector(0, 12, 0), 0, False, 0),
    lgsvl.DriveWaypoint(lgsvl.Vector( 402.9, 0, 129.2), 5, lgsvl.Vector(0, -1, 0), 0, False, 0),
    lgsvl.DriveWaypoint(lgsvl.Vector( 402.9, 0, 131.2), 5, lgsvl.Vector(0, -12, 0), 0, False, 0),
    lgsvl.DriveWaypoint(lgsvl.Vector( 402.4, 0, 132.6), 5, lgsvl.Vector(0, -23, 0), 0, False, 0),
    lgsvl.DriveWaypoint(lgsvl.Vector( 401.4, 0, 133.6), 5, lgsvl.Vector(0, -40, 0), 0, False, 0),
    lgsvl.DriveWaypoint(lgsvl.Vector( 400.3, 0, 134.9), 5, lgsvl.Vector(0, -55, 0), 0, False, 0),
    lgsvl.DriveWaypoint(lgsvl.Vector( 387.2, 0, 140.1), 5, lgsvl.Vector(0, -65, 0), 0, False, 0),
    lgsvl.DriveWaypoint(lgsvl.Vector( 382.6, 0, 142.4), 5, lgsvl.Vector(0, -51, 0), 0, False, 0),
    lgsvl.DriveWaypoint(lgsvl.Vector( 380, 0, 144), 5, lgsvl.Vector(0, -27, 0), 0, True, 15),
    lgsvl.DriveWaypoint(lgsvl.Vector( 378.7, 0, 151.1), 10, lgsvl.Vector(0, -26, 0), 0, False, 0),
    lgsvl.DriveWaypoint(lgsvl.Vector( 377.6, 0, 153.5), 10, lgsvl.Vector(0, -37, 0), 0, False, 0),
    lgsvl.DriveWaypoint(lgsvl.Vector( 354.6, 0, 165.2), 5, lgsvl.Vector(0, -63, 0), 0, False, 0),
    lgsvl.DriveWaypoint(lgsvl.Vector( 332.4, 0, 176.5), 5, lgsvl.Vector(0, -60, 0), 0, False, 0),
    lgsvl.DriveWaypoint(lgsvl.Vector( 307.4, 0, 189.), 5, lgsvl.Vector(0, -60, 0), 0, False, 0)
]
state.transform.position = waypoints[0].position
state.transform.rotation = lgsvl.Vector( 0, 21, 0)
NPC3 = sim.add_agent("Motor", lgsvl.AgentType.NPC, state)
NPC3.follow(waypoints , loop=False)

#NPC car
waypoints  = [
    lgsvl.DriveWaypoint(lgsvl.Vector( 397, 0, 131.5), 5, lgsvl.Vector(0, 21, 0), 0, False, 32),
    lgsvl.DriveWaypoint(lgsvl.Vector( 426, 0, 206.5), 5, lgsvl.Vector(0, 21, 0), 0, False, 0)
]
state.transform.position = lgsvl.Vector( 382, 0.1, 94.6)
state.transform.rotation = lgsvl.Vector( 0, 21, 0)
NPC4 = sim.add_agent("Sedan", lgsvl.AgentType.NPC, state)
NPC4.follow(waypoints , loop=False)

input("Press Enter to run")
sim.run() 

