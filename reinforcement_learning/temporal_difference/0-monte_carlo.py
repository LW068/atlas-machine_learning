#!/usr/bin/env python3
"""Monte Carlo!!!!!!!!!!"""
import numpy as np


def monte_carlo(env, V, policy, episodes=5000, max_steps=100, alpha=0.1, gamma=0.99):
    """
    Perform the Monte Carlo algorithm for value estimation.
    """
    for episode_index in range(episodes):
        current_state = env.reset()
        # handling different types of state representations:
        current_state = current_state[0] if isinstance(current_state, tuple) else current_state

        episode_data = {
            'states': [],
            'rewards': []
        }

        for step in range(max_steps):
            action = policy(current_state)
            result = env.step(action)
            next_state, reward, done, *_ = result  # Adjusted unpacking

            episode_data['states'].append(current_state)
            episode_data['rewards'].append(reward)

            if done:
                break

            current_state = next_state[0] if isinstance(next_state, tuple) else next_state

        total_return = 0
        # iterating backwards through the episode data:
        for state, reward in zip(reversed(episode_data['states']), reversed(episode_data['rewards'])):
            total_return = gamma * total_return + reward
            value_delta = total_return - V[state]
            V[state] += alpha * value_delta

    return V