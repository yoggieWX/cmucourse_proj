'''
Records a human controlled trajectory for a skill. Saves it for fitting of a DMP.
roslaunch locobot_control main.launch use_arm:=true torque_control:=true use_rviz:=false
python3 record_traj.py
'''

import time
import numpy as np

from pyrobot import Robot

# Time in seconds to record for
DURATION = 3

arm_config = dict(control_mode='torque')
robot = Robot('locobot', arm_config=arm_config)

# Set torques to 0 for human control
# TODO: need to move arm to above paper first?
target_torque = 4 * [0]
robot.arm.set_joint_torques(target_torque)

# Main loop to record trajectory
# TODO: need to save rpy?
ee_pos_array = []
velocity_array = []
acc_array = []
time_array = []
elaptime = 0

print("Goto start position")
time.sleep(5)
print("3...")
time.sleep(1)
print("2....")
time.sleep(1)
print("1....")
time.sleep(1)
print("starting to record")

start = time.time()
while elaptime < DURATION:
    pos = robot.arm.pose_ee[0]
    time_array.append(elaptime)
    ee_pos_array.append(pos)
    elaptime = time.time() - start

# Save both arrays. auto saves to .npz 
filename = input('Save as: ')
np.savez(filename, time=time_array, pos=ee_pos_array)