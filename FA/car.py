import sys
sys.path.insert(0,'/Users/andrew/Library/Python/2.7/lib/python/site-packages/')
import numpy as np

import gym
from matplotlib import pyplot as plt

env = gym.envs.make("MountainCar-v0")

a_left = 0
a_neutral = 1
a_right = 2

state = env.reset()

for step in range(300):

    #print state
    env.render(mode='rgb_array')

    action = a_neutral
    pos = state[0]
    vel = state[1]
    if pos < 0:
        if vel >= 0:
            action = a_right
        else:
            action = a_left
    if pos > 0:
        if vel >= 0:
            action = a_right
        else:
            action = a_left
    state, reward, done, info = env.step( action )
    if done:
        break

print step
env.close()
