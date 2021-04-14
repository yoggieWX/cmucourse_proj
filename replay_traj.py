'''
Replays the recorded trajectory by end effector position.
roslaunch locobot_control main.launch use_arm:=true torque_control:=false use_rviz:=false
python3 replay_traj.py
'''

import time
import numpy as np

from pyrobot import Robot

robot = Robot('locobot')

# Load recordings.
filename = 'test.npz'
times = np.load(filename)['time']
positions = np.load(filename)['pos']
print(f'Number of points: {len(positions)}')
# import pdb;pdb.set_trace()

for position in positions:
    position = position.tolist()
    robot.arm.set_ee_pose_pitch_roll(position, pitch=1.57, roll=0, plan=True)
    time.sleep(0.1)
    # print(position)
