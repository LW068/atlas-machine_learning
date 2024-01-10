#!/usr/bin/env python3
"""
module to implement the epsilon-greedy policy
"""

import numpy as np

def epsilon_greedy(Q, state, epsilon):
    """
    determines the next action using epsilon-greedy policy.
    """
    if np.random.uniform(0, 1) < epsilon:
        # Exploration: choose a random action
        action = np.random.randint(Q.shape[1])
    else:
        # Exploitation: choose the best action from Q-table at the current state
        action = np.argmax(Q[state])

    return action
