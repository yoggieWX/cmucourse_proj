'''
Replays the recorded trajectory by end effector position.
'''

import time
import numpy as np
from pyrobot import Robot

robot = Robot('locobot')

filename = 'tpy.npz'
times = np.load(filename)['time']
positions = np.load(filename)['pos']
# import pdb;pdb.set_trace()
# 	for position in positions:
    #robot.arm.set_ee_pose_pitch_roll(position.tolist(), pitch=1.57, roll=0, plan=True)

    # time.sleep(0.5)
    # print(position.tolist())
    # TODO: test if need to change position to list
orientation = np.array([[0.0,0.0, 1],[0,1,0],[-1,0,0]])
robot.arm.set_ee_pose(np.array([0.22933662,  0.08063975,  0.23528934]),orientation, plan=True)
# time.sleep(0.5)
robot.arm.set_ee_pose(np.array([ 0.22933662,  0.08063975,  0.23528934]),orientation, plan=True)
# time.sleep(0.5)
robot.arm.set_ee_pose(np.array([ 0.27959574,  0.08063975,  0.23528934]),orientation, plan=True)
# time.sleep(0.5)
robot.arm.set_ee_pose(np.array([ 0.30621406, 0.08063975,  0.23528934]),orientation, plan=True)
# time.sleep(0.5)
robot.arm.set_ee_pose(np.array([ 0.33699812, 0.08063975,  0.23528934]),orientation, plan=True)
# time.sleep(0.5)
robot.arm.set_ee_pose(np.array([ 0.36403111, 0.08063975,  0.23528934]),orientation, plan=True)
# time.sleep(0.5)
robot.arm.set_ee_pose(np.array([ 0.39949651,  0.08063975,  0.23528934]),orientation, plan=True)


