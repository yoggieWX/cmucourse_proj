'''
Replays the recorded trajectory by end effector position.
'''

import numpy as np
from pyrobot import Robot

robot = Robot('locobot')

filename = 'line.npy'
times = np.load(filename)['time']
positions = np.load(filename)['pos']

for position in positions:
    robot.arm.set_ee_pose_pitch_roll(position, pitch=1.57, roll=0, plan=True)
    # TODO: test if need to change position to list

