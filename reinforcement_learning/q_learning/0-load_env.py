#!/usr/bin/env python3
"""
Module to load the Frozen Lake environment using OpenAI Gym
"""

import gym
from gym.envs.toy_text.frozen_lake import generate_random_map


def load_frozen_lake(custom_desc=None, chosen_map=None, slippery_surface=False):
    """
    Loadign the FrozenLakeEnv environment from OpenAI's gym with specified parameters
    """
    if custom_desc is None and chosen_map is None:
        size = 8  # Default size for a random map
        custom_desc = generate_random_map(size=size, p=0.8)  # p is the probability of a tile being frozen

    if custom_desc is not None:
        # creating a custom FrozenLake environment with the given description
        env = gym.make("FrozenLake-v1", desc=custom_desc, is_slippery=slippery_surface)
    else:
        # loading a pre-made mapo
        env = gym.make(f"FrozenLake-{chosen_map}-v1", is_slippery=slippery_surface)

    return env
