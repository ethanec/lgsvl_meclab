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

#NPC Vehicle
waypoints_1 = [
  lgsvl.DriveWaypoint(lgsvl.Vector(6777.276,-63.11819,-8185.542), 6, lgsvl.Vector(0, 155.038, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6782.998,-63.11819,-8197.882), 6, lgsvl.Vector(0, 155.039, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6789.814,-63.11819,-8212.432), 6, lgsvl.Vector(0, 155.039, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6794.949,-63.11818,-8222.287), 6, lgsvl.Vector(0, 155.039, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6800.361,-63.11819,-8235.233), 6, lgsvl.Vector(0, 155.039, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6803.55,-63.11819,-8241.354), 6, lgsvl.Vector(0, 148.856, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6804.363,-63.11819,-8242.526), 6, lgsvl.Vector(0, 145.916, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6805.169,-63.11819,-8243.455), 6, lgsvl.Vector(0, 141.063, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6806.363,-63.11819,-8244.345), 6, lgsvl.Vector(0, 129.835, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6806.842,-63.11819,-8244.593), 6, lgsvl.Vector(0, 125.548, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6807.657,-63.11819,-8244.903), 6, lgsvl.Vector(0, 118.503, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6808.686,-63.11819,-8245.132), 6, lgsvl.Vector(0, 90.08, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6809.464,-63.11819,-8243.771), 6, lgsvl.Vector(0, 57.901, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6811.068,-63.11819,-8241.24), 6, lgsvl.Vector(0, 30.569, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6810.882,-63.11819,-8240.451), 6, lgsvl.Vector(0, 13.101, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6810.25,-63.11819,-8239.472), 6, lgsvl.Vector(0, -11.374, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6809.721,-63.11819,-8238.965), 6, lgsvl.Vector(0, -24.521, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6809.218,-63.11819,-8238.105), 6, lgsvl.Vector(0, -27.942, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6808.438,-63.11819,-8236.877), 6, lgsvl.Vector(0, -30.579, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6805.782,-63.11819,-8231.729), 6, lgsvl.Vector(0, -24.865, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6783.498,-63.11819,-8185.141), 6, lgsvl.Vector(0, -24.522, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6782.357,-63.11819,-8182.973), 6, lgsvl.Vector(0, -27.293, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6780.673,-63.11819,-8180.569), 6, lgsvl.Vector(0, -35.844, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6779.406,-63.11819,-8180.355), 6, lgsvl.Vector(0, -61.637, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6778.613,-63.11819,-8180.475), 6, lgsvl.Vector(0, -76.286, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6777.588,-63.11819,-8181.002), 6, lgsvl.Vector(0, -98.22101, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6776.818,-63.11819,-8181.862), 6, lgsvl.Vector(0, -119.244, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6776.361,-63.11819,-8182.795), 6, lgsvl.Vector(0, -135.619, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6776.314,-63.11819,-8183.423), 6, lgsvl.Vector(0, -148.541, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6776.429,-63.11819,-8184.234), 6, lgsvl.Vector(0, -164.772, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6776.784,-63.11819,-8185.022), 6, lgsvl.Vector(0, -181.672, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6777.239,-63.11819,-8185.53), 6, lgsvl.Vector(0, -195.32, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6777.656,-63.11819,-8186.017), 6, lgsvl.Vector(0, -203.445, 0), 0, True, 0)
]

waypoints_2 = [
  lgsvl.DriveWaypoint(lgsvl.Vector(6773.772,-63.11819,-8186.84), 6, lgsvl.Vector(0, 155.149, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6779.453,-63.11819,-8198.893), 6, lgsvl.Vector(0, 155.149, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6786.146,-63.11819,-8213.565), 6, lgsvl.Vector(0, 155.15, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6791.633,-63.11819,-8224.785), 6, lgsvl.Vector(0, 155.541, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6796.898,-63.11819,-8236.095), 6, lgsvl.Vector(0, 155.114, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6800.704,-63.11819,-8243.927), 6, lgsvl.Vector(0, 152.174, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6803.813,-63.11819,-8248.36), 6, lgsvl.Vector(0, 137.816, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6806.455,-63.11819,-8249.819), 6, lgsvl.Vector(0, 121.221, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6810.131,-63.11819,-8250.518), 6, lgsvl.Vector(0, 89.23901, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6811.925,-63.11819,-8249.365), 6, lgsvl.Vector(0, 62.932, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6813.925,-63.11819,-8246.058), 6, lgsvl.Vector(0, 27.973, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6814.455,-63.11819,-8243.317), 6, lgsvl.Vector(0, 8.063001, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6814.087,-63.11819,-8241.905), 6, lgsvl.Vector(0, -6.459, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6813.546,-63.11819,-8240.425), 6, lgsvl.Vector(0, -15.491, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6811.715,-63.11819,-8235.849), 6, lgsvl.Vector(0, -23.796, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6808.996,-63.11819,-8229.952), 6, lgsvl.Vector(0, -24.606, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6785.896,-63.11819,-8182.028), 6, lgsvl.Vector(0, -26.718, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6782.738,-63.11819,-8177.411), 6, lgsvl.Vector(0, -40.943, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6780.488,-63.11819,-8176.088), 6, lgsvl.Vector(0, -56.943, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6778.854,-63.11819,-8175.877), 6, lgsvl.Vector(0, -75.312, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6774.893,-63.11819,-8178.032), 6, lgsvl.Vector(0, -129.841, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6772.847,-63.11819,-8180.758), 6, lgsvl.Vector(0, -146.807, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6772.529,-63.11819,-8183.266), 6, lgsvl.Vector(0, -171.987, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6772.949,-63.11819,-8184.988), 6, lgsvl.Vector(0, -187.973, 0), 0, True, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(6773.58,-63.11819,-8186.063), 6, lgsvl.Vector(0, -201.24, 0), 0, True, 0)
]

def waypoint_minus(waypoint_a, waypoint_b, interval):
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
  smooth_waypoints.append(lgsvl.DriveWaypoint(lgsvl.Vector(x,y,z), 6, lgsvl.Vector(0, yaw, 0), 0, True, 0))

  for i in range(len(waypoints)-1):
    waypoint_vec = waypoint_minus(waypoints[i], waypoints[i+1], interval)

    for j in range(interval):
      x = x + waypoint_vec[0]
      y = y + waypoint_vec[1]
      z = z + waypoint_vec[2]
      yaw = yaw + waypoint_vec[3]
      # print(temp.angle)
      smooth_waypoints.append(lgsvl.DriveWaypoint(lgsvl.Vector(x,y,z), 6, lgsvl.Vector(0, yaw, 0), 0, True, 0))

  # for i in range(len(smooth_waypoints)):
  #   print(i, smooth_waypoints[i].angle)

  return smooth_waypoints
interval = 5
smooth_waypoints_1 = smooth(waypoints_1, interval)

state.transform.position = waypoints_1[0].position
state.transform.rotation = waypoints_1[0].angle
npc1 = sim.add_agent('SUV', lgsvl.AgentType.NPC, state)

state.transform.position = waypoints_1[1].position
state.transform.rotation = waypoints_1[1].angle
npc2 = sim.add_agent('Sedan', lgsvl.AgentType.NPC, state)

state.transform.position = waypoints_1[2].position
state.transform.rotation = waypoints_1[2].angle
npc3 = sim.add_agent('Motor', lgsvl.AgentType.NPC, state)

state.transform.position = waypoints_1[3].position
state.transform.rotation = waypoints_1[3].angle
npc4 = sim.add_agent('Jeep', lgsvl.AgentType.NPC, state)

state.transform.position = waypoints_1[4].position
state.transform.rotation = waypoints_1[4].angle
npc5 = sim.add_agent('Hatchback', lgsvl.AgentType.NPC, state)


smooth_waypoints_2 = smooth(waypoints_2, interval)

state.transform.position = waypoints_2[0].position
state.transform.rotation = waypoints_2[0].angle
npc6 = sim.add_agent('Hatchback', lgsvl.AgentType.NPC, state)

state.transform.position = waypoints_2[1].position
state.transform.rotation = waypoints_2[1].angle
npc7 = sim.add_agent('SUV', lgsvl.AgentType.NPC, state)

state.transform.position = waypoints_2[2].position
state.transform.rotation = waypoints_2[2].angle
npc8 = sim.add_agent('Jeep', lgsvl.AgentType.NPC, state)

state.transform.position = waypoints_2[3].position
state.transform.rotation = waypoints_2[3].angle
npc9 = sim.add_agent('Motor', lgsvl.AgentType.NPC, state)

state.transform.position = waypoints_2[4].position
state.transform.rotation = waypoints_2[4].angle
npc10 = sim.add_agent('Sedan', lgsvl.AgentType.NPC, state)


# 11.1 m/s is ~40 km/h , 5.6 m/s is ~20 km/h
#Activity NPC
# npc1.follow_closest_lane(True, 5.5)

npc1.follow(smooth_waypoints_1,loop=True)
npc2.follow(smooth_waypoints_1,loop=True)
npc3.follow(smooth_waypoints_1,loop=True)
npc4.follow(smooth_waypoints_1,loop=True)
npc5.follow(smooth_waypoints_1,loop=True)

npc6.follow(smooth_waypoints_2,loop=True)
npc7.follow(smooth_waypoints_2,loop=True)
npc8.follow(smooth_waypoints_2,loop=True)
npc9.follow(smooth_waypoints_2,loop=True)
npc10.follow(smooth_waypoints_2,loop=True)


input("Press Enter to run")

sim.run() 
