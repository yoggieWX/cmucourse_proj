'''
Load joint angles from pickle file and prints values
TODO: add function to replay saved tracjectory
'''

import pickle

from pyrobot import Robot

robot = Robot('locobot')

#position = [0.418, -0.118, 0.257]
#robot.arm.set_ee_pose_pitch_roll(position, pitch=1.57, roll=0, plan=True)

# Load from pickle file
with open('touch.p','rb') as f:
    demoTime = pickle.load(f)
    demoJoint = pickle.load(f)

# Print joint angles
for item in demoJoint:
	print(item)
