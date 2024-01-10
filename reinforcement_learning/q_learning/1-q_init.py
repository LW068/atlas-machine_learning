#!/usr/bin/env python3
"""
module to initialize the Q-table for the Frozen Lake environment
"""

import numpy as np


def q_init(env):
    """
    Initializes the Q-table for the FrozenLakeEnv environment
    """
    number_of_states = env.observation_space.n
    number_of_actions = env.action_space.n
    q_table = np.zeros((number_of_states, number_of_actions))

    return q_table