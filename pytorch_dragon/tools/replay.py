"""
Pytorch reinforcement learning action replay sampling functions
"""

import torch as T
import numpy as np


class OUActionNoise(object):
    def __init__(self, mu, sigma=0.05, theta=0.1, dt=1e-2, x0=None):
        """
        Temporally local, continous distribution sampler for exploration vs exploitation problem (Phil Tabour)
        """
        self.theta = theta
        self.mu = mu
        self.sigma = sigma
        self.dt = dt
        self.x0 = x0
        self.reset()

    def __call__(self):
        x = (
            self.x_prev
            + self.theta * (self.mu - self.x_prev) * self.dt
            + self.sigma * np.sqrt(self.dt) * np.random.normal(size=self.mu.shape)
        )
        self.x_prev = x
        return x

    def reset(self):
        self.x_prev = self.x0 if self.x0 is not None else np.zeros_like(self.mu)

    def __repr__(self):
        return "OrnsteinUhlenbeckActionNoise(mu={}, sigma={})".format(
            self.mu, self.sigma
        )
