#!/usr/bin/env python3
#
# Copyright (c) 2019 LG Electronics, Inc.
#
# This software contains code licensed as described in LICENSE.
#

import os
import lgsvl
import random
import time

sim = lgsvl.Simulator(os.environ.get("SIMULATOR_HOST", "127.0.0.1"), 8181)
if sim.current_scene == "BorregasAve":
  sim.reset()
else:
  sim.load("BorregasAve")

spawns = sim.get_spawn()

tr = spawns[0]
print("Default transform: {}".format(tr))

# There are functions to convert to and from GPS coordingates
# This function takes position and rotation vectors and outputs the equivalent GPS coordinates
gps = sim.map_to_gps(tr)
print("GPS coordinates: {}".format(gps))

# This function can take either lat/long or northing/easting pairs as inputs and will provide equivalent position and rotation vectors
# Altitude and orientation are optional
t1 = sim.map_from_gps(northing = gps.northing, easting = gps.easting, altitude = gps.altitude, orientation = gps.orientation)
print("Transform from northing/easting: {}".format(t1))

t2 = sim.map_from_gps(latitude = gps.latitude, longitude = gps.longitude)
print("Transform from lat/long without altitude/orientation: {}".format(t2))
