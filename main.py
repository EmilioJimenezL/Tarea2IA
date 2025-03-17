import gymnasium as gym
import numpy as np

env = gym.make('Blackjack-v1', sab=True, render_mode = "rgb_array")
obs,info = env.reset()