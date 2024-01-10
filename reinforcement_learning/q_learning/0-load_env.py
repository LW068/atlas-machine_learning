#!/usr/bin/env python3
"""
Module to load the Frozen Lake environment using OpenAI Gym
"""

import gym
from gym.envs.toy_text.frozen_lake import generate_random_map


def load_frozen_lake(desc=None, map_name=None, is_slippery=False):
    """
    Loadign the FrozenLakeEnv environment from OpenAI's gym with specified parameters
    """
    # If a custom description is provided, generate a random map
    if desc is not None:
        size = 8  # Default size for a random map
        desc = generate_random_map(size=size, p=0.8)

    # Create the environment
    env = gym.make("FrozenLake-v1",
                   map_name, desc=desc, is_slippery=is_slippery)

    return env
