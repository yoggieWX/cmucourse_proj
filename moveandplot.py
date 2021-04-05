from pyrobot import Robot
import time
import numpy as np
import matplotlib.pyplot as plt

robot = Robot('locobot')

# position = [0.418, 0., 0.23]

position=np.array([0.418, 0.0, 0.15])
position1=np.array([-0.20, 0.0, 0.0])
orientation=np.array([[0.0,0.0,1.0],[0.0,1.0,0.0],[-1,0.0,0.0]])

# start position
robot.arm.set_ee_pose_pitch_roll([0.418, 0., 0.20], pitch=1.57, roll=0, plan=True)
time.sleep(2)
# robot.arm.set_ee_pose(position, orientation, plan=True, wait=True)
# robot.arm.move_ee_xyz(position1, plan=False, numerical=False)
# time.sleep(2)

ee_pos = []
Time=[]
start = time.time()
snooze = time.time()
# position2=np.array([0.0, 0.15, 0.0])
# time.sleep(2)
# robot.arm.move_ee_xyz(position2, plan=False, numerical=False)
for i in range(7):
	# position2 = np.array([-0.02, 0, 0])
	# robot.arm.move_ee_xyz(position2, plan=False, numerical=False)

	# robot.arm.set_ee_pose_pitch_roll([0.418 - 0.02 * i, 0.0, 0.15], pitch=1.57, roll=0, plan=False, wait=False)
	position=np.array([0.418-0.02*i, 0.0, 0.15])
	orientation=np.array([[0.0,0.0,1.0],[0.0,1.0,0.0],[-1,0.0,0.0]])
	robot.arm.set_ee_pose(position, orientation, plan=False, wait=False)
	# robot.arm.move_ee_xyz(position, plan=False, numerical=False)
	while time.time() - snooze < 2:
		elaptime = time.time() - start
		pos = robot.arm.pose_ee[0]
		Time.append(elaptime)
		ee_pos.append(pos)
	snooze = time.time()
fig,axes = plt.subplots(3)

axes[0].plot(Time, [ee_pos[i][0] for i in range(len(ee_pos))])
axes[1].plot(Time, [ee_pos[i][1] for i in range(len(ee_pos))])
axes[2].plot(Time, [ee_pos[i][2] for i in range(len(ee_pos))])
print(ee_pos[0], ee_pos[-1])

plt.show()

# # (array([[0.40872469],
# #        [0.00392196],
# #        [0.21296304]]), array([[-7.35591238e-02,  1.49657630e-03,  9.97289735e-01],
# #        [-9.02751605e-04,  9.99998364e-01, -1.56722707e-03],
# #        [-9.97290449e-01, -1.01558876e-03, -7.35576525e-02]]), array([ 2.02628528e-04,  7.32651885e-01, -8.81324363e-04,  6.80602966e-01]))


