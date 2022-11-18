#!/usr/bin/env python3
#
# Copyright (c) 2019 LG Electronics, Inc.
#
# This software contains code licensed as described in LICENSE.
#

import os
import lgsvl

sim = lgsvl.Simulator(os.environ.get("SIMULATOR_HOST", "127.0.0.1"), 8181)
if sim.current_scene == "BorregasAve":
  sim.reset()
else:
  sim.load("BorregasAve")

spawns = sim.get_spawn()

state = lgsvl.AgentState()
state.transform = spawns[0]
a = sim.add_agent("Lincoln2017MKZ (Apollo 5.0)", lgsvl.AgentType.EGO, state)

# get_sensors returns a list of sensors on the EGO vehicle
sensors = a.get_sensors()
for s in sensors:
  if s.name == "Main Camera":
    # Camera and LIDAR sensors can save data to the specified file path
    s.save("main-camera.png", compression=0)
    s.save("main-camera.jpg", quality=75)
    break
