#!/usr/bin/env python3
"""
Module to train an agent using the Q-learning algorithm
"""

import numpy as np

def train(env, Q, episodes=5000, max_steps=100, alpha=0.1, gamma=0.99, epsilon=1, min_epsilon=0.1, epsilon_decay=0.05):
    """
    Performs Q-learning on an environment with a given Q-table.
    """
    total_rewards = []

    for episode in range(episodes):
        state = env.reset()
        episode_rewards = 0

        for step in range(max_steps):
            # Epsilon-greedy action selection
            if np.random.rand() < epsilon:
                action = np.random.randint(0, env.action_space.n)
            else:
                action = np.argmax(Q[state])

            new_state, reward, done, _ = env.step(action)

            # Update reward for falling in a hole
            if done and reward == 0:
                reward = -1

            # Q-learning formula
            Q[state, action] = Q[state, action] + alpha * (reward + gamma * np.max(Q[new_state]) - Q[state, action])

            state = new_state
            episode_rewards += reward

            if done:
                break

        # Epsilon decay
        epsilon = max(min_epsilon, epsilon - epsilon_decay)
        total_rewards.append(episode_rewards)

    return Q, total_rewards