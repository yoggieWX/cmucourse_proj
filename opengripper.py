'''
Use this script to insert/ remove tool from the robot gripper. 
type 'open' or 'close' when prompted.
'''

import json
from pyrobot import Robot

robot = Robot('locobot')

# Move to start position.
robot.arm.set_ee_pose_pitch_roll([0.418, 0., 0.25], pitch=1.57, roll=0, plan=True)

def open_gripper():
    robot.gripper.open()

def close_gripper():
    robot.gripper.close()

def move(position):
    robot.arm.set_ee_pose_pitch_roll(position, pitch=1.57, roll=0, plan=True)

while True:
    command = input("Command (open, close, move): ")
    if command.lower() == 'open':
        open_gripper()
    elif command.lower() == 'close':
        close_gripper()
    elif command.lower() == 'move':
        position = input('Enter a list [x,y,z]: ')
        position = json.loads(position)
        move(position)
    else:
        print('please enter a valid command.')
    # TODO: add exit command