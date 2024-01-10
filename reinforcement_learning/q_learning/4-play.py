#!/usr/bin/env python3
"""
Module to simulate a gaemplay in the Frozen Lake environment using a trained Q-table
"""

def play(env, Q, max_steps=100):
    """
    Has the trained agent play an episode
    """
    state = env.reset()
    total_rewards = 0

    for step in range(max_steps):
        # selects the best action (exploit)
        action = np.argmax(Q[state])

        # Takign the action
        new_state, reward, done, _ = env.step(action)

        # Displays the current state of the environment
        env.render()

        total_rewards += reward
        state = new_state

        if done:
            break

    return total_rewards
