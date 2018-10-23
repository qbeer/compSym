# OOP decay
import numpy as np
import matplotlib.pyplot as plt

class DecayingParticles:
    def __init__(self, number_of_particles, lamb):
        self.number_of_particles = number_of_particles
        self.lamb = lamb
        self.decayed_states = None

    def __repr__(self):
        return "The system initially contained %d particles and it decayed with a rate of %.5f" % (self.number_of_particles, self.lamb)

    def decay(self):
        N = self.number_of_particles
        time_decayed_remainder = []
        t = 0
        while N > 0:
            decayed = 0
            for i in range(0, N):
                if np.random.random_sample() < self.lamb :
                    decayed += 1
            t += 1 # time
            N -= decayed
            time_decayed_remainder.append([t, decayed, N])
        self.decayed_states = np.array(time_decayed_remainder)
        return self

    def plot(self):
        if self.decayed_states.all() == None:
            self = self.decay()
        plt.figure(figsize=(12, 5))
        time = self.decayed_states[:, 0]
        decayed = self.decayed_states[:, 1]
        remained = self.decayed_states[:, 2]
        plt.plot(time, decayed, 'bx--', label='Decayed')
        plt.plot(time, remained, 'ro--', label='Remaining')
        plt.title('Radioactive system')
        plt.xlabel('t [mikro s]')
        plt.ylabel('N')
        plt.legend(loc='upper right')
        plt.show()

system = DecayingParticles(12500, 0.3).decay()
print(system)
system.plot()