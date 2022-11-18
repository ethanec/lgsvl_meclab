# -*- coding: utf-8 -*-
"""
@author: Chen-Xuan LIN
NCKU Intersection Sacenario
Sacenario : Motorcycle cut in from right side
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
state.transform.position = lgsvl.Vector( 398.2, 0.1, 167.34)
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
state.transform.position = lgsvl.Vector( 395.4, 0.1, 162.7)
state.transform.rotation = lgsvl.Vector( 0, -157.4, 0)
NPC3 = sim.add_agent("Motor", lgsvl.AgentType.NPC, state)
state.transform.position = lgsvl.Vector( 397.1, 0.1, 163.4)
state.transform.rotation = lgsvl.Vector( 0, -157.4, 0)
NPC4 = sim.add_agent("Motor", lgsvl.AgentType.NPC, state)

NPC.follow_closest_lane(True, 5.6)
NPC2.follow_closest_lane(True, 5.6)
NPC3.follow_closest_lane(True, 5.6)
NPC4.follow_closest_lane(True, 5.6)


#Motor follow the waypoints
waypoints  = [
    lgsvl.DriveWaypoint(lgsvl.Vector( 394.7, 0, 166.9), 5, lgsvl.Vector(0, -157.4, 0), 21, False, 0),
    lgsvl.DriveWaypoint(lgsvl.Vector( 392.2, 0, 160.4), 5, lgsvl.Vector(0, -157.4, 0), 0, False, 0),
    lgsvl.DriveWaypoint(lgsvl.Vector( 392.1, 0, 158.4), 5, lgsvl.Vector(0, -167.4, 0), 0, False, 0),
    lgsvl.DriveWaypoint(lgsvl.Vector( 392, 0, 157.2), 5, lgsvl.Vector(0, -176.5, 0), 0, False, 0),
    lgsvl.DriveWaypoint(lgsvl.Vector( 392.3, 0, 153.4), 5, lgsvl.Vector(0, -164.1, 0), 0, False, 0),
    lgsvl.DriveWaypoint(lgsvl.Vector( 370.8, 0, 100.7), 5, lgsvl.Vector(0, -165.4, 0), 0, False, 0)
]
state.transform.position = lgsvl.Vector( 394.7, 0.1, 166.9)
state.transform.rotation = lgsvl.Vector( 0, -157.4, 0)
NPC5 = sim.add_agent("Motor", lgsvl.AgentType.NPC, state)
NPC5.follow(waypoints , loop=False)

#NPC car
waypoints  = [
    lgsvl.DriveWaypoint(lgsvl.Vector( 397, 0, 131.5), 5, lgsvl.Vector(0, 21, 0), 0, False, 32),
    lgsvl.DriveWaypoint(lgsvl.Vector( 426, 0, 206.5), 5, lgsvl.Vector(0, 21, 0), 0, False, 0)
]
state.transform.position = lgsvl.Vector( 382, 0.1, 94.6)
state.transform.rotation = lgsvl.Vector( 0, 21, 0)
Car = sim.add_agent("Sedan", lgsvl.AgentType.NPC, state)
Car.follow(waypoints , loop=False)

input("Press Enter to run")
sim.run() 

