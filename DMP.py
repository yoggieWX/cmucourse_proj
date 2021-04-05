import math
import numpy as np

class DMP:
    def __init__(self, num_basis):
        self.K = 25 * 25 / 4
        self.B = 25
        self.centers = np.linspace(0, 1, num_basis) # Basis function centers
        self.width = (0.65 * (1. / (num_basis - 1.)) ** 2) # Basis function widths
        self.duration = 3
        self.dt = 0.003

    def learn_weights(self, filename):
        '''
        From  recorded disp, vel and acc datas, learn DMP weights 
        '''
        data = np.load(filename)
        times = data['time']
        disps = data['pos']
        vels = data['vel']
        accs = data['acc']
        duration = times[-1]

        PHI = []
        forcing_function = []
        for i, time in enumerate(times):
            phi = [math.exp(-0.5 * ((time / duration) - center) ** 2 / self.width) for center in self.centers]
            phi = phi / np.sum(phi)
            PHI.append(phi)

            f = ((accs[i] * duration ** 2) - self.K * (disps[-1] - disps[i]) + self.B * (vels[i] * duration)) / (disps[-1] - disp[0])
            forcing_function.append(f)

        # Calculate weights via linear regression
        self.weights = np.matmul(np.matmul(np.linalg.inv(np.matmul(np.transpose(PHI),PHI)),np.transpose(PHI)),F)

        # Save the weights file to save relearning time
        np.save('DMPweights.npy', weights=self.weights)

    def load_weights(self, filename):
        '''
        Load weights from npy file
        '''
        self.weights = np.load(filename)['weights']

    def generate_traj(self, start, goal):
        '''
        From learned weights, generate a trajectory from start to goal.
        start, goal: python list of floats xyz positions
        '''
        pose_start = np.array(start)
        pose = np.copy(pose_start)
        pose_goal = np.array(goal)
        vel = np.zeros(3)
        acc = np.zeros(3)
        dmp_trajectory = np.zeros(2000)
        dmp_trajectory[0] = (pose_start)

        t = 0
        for i in range(2000):
            t = t + self.dt
            if t < self.duration:
                Phi = [math.exp(-0.5 * ((t/self.duration) - center) ** 2 / self.width) for center in self.centers]
                Phi = Phi / np.sum(Phi)
                force = np.dot(Phi, self.weights)
            else: 
                force = 0
            acc = self.K * (pose_goal - pose) / (self.duration ** 2) - self.B * vel / self.duration + (pose_goal - pose_start) * force / (self.duration ** 2)
            vel = vel + acc * self.dt
            # import pdb;pdb.set_trace()
            pose = pose + vel * self.dt
            dmp_trajectory[i] = pose

        return dmp_trajectory


if __name__ = "__main__":
    DMP = DMP(5)
    DMP.learn_weights('line.npy')
    # DMP.load_weights('DMPweights.npy')
    trajectory = DMP.generate_traj([0.438, 0, 0.25], [0.338, 0, 0.25])
    # TODO: set position directly in generate_traj?
    for position in trajectory:
        robot.arm.set_ee_pose_pitch_roll(position, pitch=1.57, roll=0, plan=True)
