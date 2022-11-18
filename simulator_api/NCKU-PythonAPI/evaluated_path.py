# -*- coding: utf-8 -*-
import os
import lgsvl
import time

# Load Map
sim = lgsvl.Simulator(os.environ.get("SIMULATOR_HOST", "127.0.0.1"), 8181)
if sim.current_scene == "Shalun":
  sim.reset()
else:
  sim.load("Shalun")
spawns = sim.get_spawn()

# ego Vehicle
state = lgsvl.AgentState()
state.transform.position.x = 6769.801
state.transform.position.y = -63.11819
state.transform.position.z = -8162.083
state.transform.rotation.y = 154.54
ego = sim.add_agent("NCKU-Lincoln_MKZ", lgsvl.AgentType.EGO, state)

# ego vehicle attach Autoware IP and Port
connect = input("Connect to autoware y (yes), n (no) :")
if connect == "y":
  ego.connect_bridge(os.environ.get("BRIDGE_HOST", "192.168.0.147"), 9090)
  print("Waiting for connection...")
  while not ego.bridge_connected:
    print("Bridge connecting...")
    time.sleep(1)
  print("Bridge connected:", ego.bridge_connected)

velocity = 4

  #NPC Vehicle
waypoints = [
  lgsvl.DriveWaypoint(lgsvl.Vector(6762.913,-63.11819,-8182.219), velocity, lgsvl.Vector(0, -114.68, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6747.628,-63.11819,-8189.359), velocity, lgsvl.Vector(0, -115.671, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6743.203,-63.11819,-8191.566), velocity, lgsvl.Vector(0, -117.263, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6739.357,-63.11819,-8193.919), velocity, lgsvl.Vector(0, -123.609, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6736.573,-63.11819,-8196.278), velocity, lgsvl.Vector(0, -133.188, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6735.275,-63.11819,-8198.343), velocity, lgsvl.Vector(0, -144.464, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6734.569,-63.11819,-8200.079), velocity, lgsvl.Vector(0, -156.923, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6734.053,-63.11819,-8201.911), velocity, lgsvl.Vector(0, -163.017, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6733.848,-63.11819,-8204.007), velocity, lgsvl.Vector(0, -174.229, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6734.112,-63.11819,-8205.18), velocity, lgsvl.Vector(0, -184.893, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6735.012,-63.11819,-8207.627), velocity, lgsvl.Vector(0, -201.39, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6737.298,-63.11819,-8213.4), velocity, lgsvl.Vector(0, -201.39, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6738.15,-63.11819,-8215.29), velocity, lgsvl.Vector(0, -203.715, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6743.013,-63.11819,-8226.156), velocity, lgsvl.Vector(0, -204.82, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6753.253,-63.11819,-8247.973), velocity, lgsvl.Vector(0, -205.429, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6777.799,-63.11819,-8299.593), velocity, lgsvl.Vector(0, -205.429, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6779.651,-63.11819,-8303.568), velocity, lgsvl.Vector(0, -205.454, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6780.478,-63.11819,-8304.685), velocity, lgsvl.Vector(0, -213.722, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6781.06,-63.11819,-8305.348), velocity, lgsvl.Vector(0, -217.605, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6782.039,-63.11819,-8306.45), velocity, lgsvl.Vector(0, -220.854, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6783.388,-63.11819,-8307.251), velocity, lgsvl.Vector(0, -234.123, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6784.731,-63.11819,-8307.782), velocity, lgsvl.Vector(0, -244.296, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6788.396,-63.11819,-8308.371), velocity, lgsvl.Vector(0, -269.416, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6789.483,-63.11819,-8308.016), velocity, lgsvl.Vector(0, -280.806, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6790.439,-63.11819,-8307.39), velocity, lgsvl.Vector(0, -293.844, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6793.392,-63.11819,-8306.044), velocity, lgsvl.Vector(0, -295.513, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6812.738,-63.11819,-8296.859), velocity, lgsvl.Vector(0, -295.513, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6815.094,-63.11819,-8296.131), velocity, lgsvl.Vector(0, -285.419, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6817.41,-63.11819,-8296.447), velocity, lgsvl.Vector(0, -263.069, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6819.908,-63.11819,-8297.11), velocity, lgsvl.Vector(0, -254.966, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6823.32,-63.11819,-8298.031), velocity, lgsvl.Vector(0, -254.966, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6825.557,-63.11819,-8298.252), velocity, lgsvl.Vector(0, -263.132, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6829.698,-63.11819,-8298.475), velocity, lgsvl.Vector(0, -269.918, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6831.837,-63.11819,-8298.057), velocity, lgsvl.Vector(0, -280.398, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6834.788,-63.11819,-8296.592), velocity, lgsvl.Vector(0, -300.106, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6836.777,-63.11819,-8294.854), velocity, lgsvl.Vector(0, -312.87, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6838.414,-63.11819,-8292.357), velocity, lgsvl.Vector(0, -331.027, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6839.445,-63.11819,-8288.859), velocity, lgsvl.Vector(0, -348.296, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6839.452,-63.11819,-8286.844), velocity, lgsvl.Vector(0, -359.055, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6838.875,-63.11819,-8283.725), velocity, lgsvl.Vector(0, -375.326, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6836.941,-63.11819,-8280.213), velocity, lgsvl.Vector(0, -36.376, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6834.423,-63.11819,-8277.717), velocity, lgsvl.Vector(0, -45.696, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6830.679,-63.11819,-8274.063), velocity, lgsvl.Vector(0, -45.586, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6829.569,-63.11819,-8272.546), velocity, lgsvl.Vector(0, -35.946, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6827.805,-63.11819,-8269.262), velocity, lgsvl.Vector(0, -25.88, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6826.34,-63.11819,-8266.42), velocity, lgsvl.Vector(0, -26.645, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6821.418,-63.11819,-8256.524), velocity, lgsvl.Vector(0, -26.135, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6819.501,-63.11819,-8253.691), velocity, lgsvl.Vector(0, -37.375, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6816.57,-63.11819,-8249.83), velocity, lgsvl.Vector(0, -37.374, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6813.178,-63.11819,-8245.029), velocity, lgsvl.Vector(0, -34.961, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6809.79,-63.11819,-8239.255), velocity, lgsvl.Vector(0, -27.794, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6803.556,-63.11819,-8226.875), velocity, lgsvl.Vector(0, -25.647, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6783.034,-63.11819,-8184.2), velocity, lgsvl.Vector(0, -25.647, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6780.427,-63.11819,-8180.245), velocity, lgsvl.Vector(0, -39.968, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6778.84,-63.11819,-8178.763), velocity, lgsvl.Vector(0, -47.592, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6776.96,-63.11819,-8177.646), velocity, lgsvl.Vector(0, -60.021, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6774.456,-63.11819,-8177.359), velocity, lgsvl.Vector(0, -80.18401, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6771.657,-63.11819,-8178.396), velocity, lgsvl.Vector(0, -111.987, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6767.563,-63.11819,-8180.218), velocity, lgsvl.Vector(0, -114.987, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6762.913,-63.11819,-8182.219), velocity, lgsvl.Vector(0, -114.68, 0), 0, True, 0)
]

def waypoint_minus(waypoint_a, waypoint_b, interval):
  # print("waypoint a :", waypoint_a.position.x, ", ", waypoint_a.position.y, ", ", waypoint_a.position.z, ", ", waypoint_a.angle.y)
  x = (waypoint_b.position.x - waypoint_a.position.x)/interval
  y = (waypoint_b.position.y - waypoint_a.position.y)/interval
  z = (waypoint_b.position.z - waypoint_a.position.z)/interval
  yaw = (waypoint_b.angle.y - waypoint_a.angle.y)/interval
  vec = [x, y, z, yaw]
  return vec

def smooth(waypoints, interval): #Interpolation
  smooth_waypoints = []
  x = waypoints[0].position.x
  y = waypoints[0].position.y
  z = waypoints[0].position.z
  yaw = waypoints[0].angle.y

  # print(temp.angle)
  smooth_waypoints.append(lgsvl.DriveWaypoint(lgsvl.Vector(x,y,z), velocity, lgsvl.Vector(0, yaw, 0), 0, True, 0))

  for i in range(len(waypoints)-1):
    waypoint_vec = waypoint_minus(waypoints[i], waypoints[i+1], interval)

    for j in range(interval):
      x = x + waypoint_vec[0]
      y = y + waypoint_vec[1]
      z = z + waypoint_vec[2]
      yaw = yaw + waypoint_vec[3]
      # print(temp.angle)
      smooth_waypoints.append(lgsvl.DriveWaypoint(lgsvl.Vector(x,y,z), velocity, lgsvl.Vector(0, yaw, 0), 0, True, 0))

  # for i in range(len(smooth_waypoints)):
  #   print(i, smooth_waypoints[i].angle)

  return smooth_waypoints

smooth_waypoints = smooth(waypoints, 10)

state.transform.position = smooth_waypoints[0].position
state.transform.rotation = smooth_waypoints[0].angle

npc1 = sim.add_agent('SUV', lgsvl.AgentType.NPC, state)

# 11.1 m/s is ~40 km/h , 5.6 m/s is ~20 km/h
#Activity NPC
# npc1.follow_closest_lane(True, 5.5)


npc1.follow(smooth_waypoints,loop=True)

input("Press Enter to run")

sim.run() 