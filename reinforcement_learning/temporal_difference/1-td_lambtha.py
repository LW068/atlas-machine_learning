#!/usr/bin/env python3
"""Lambthaaaa!!!"""
import numpy as np


def td_lambtha(env, V, policy, lambtha, episodes=5000, max_steps=100, alpha=0.1, gamma=0.99):
    """
    Perform the "TD(λ)' algorithm for value estimation.
    """
    for _ in range(episodes):
        state = env.reset()
        # Adjusting for different return types of env.reset()
        state = state[0] if isinstance(state, tuple) else state

        eligibility_trace = np.zeros_like(V)
        for _ in range(max_steps):
            action = policy(state)
            result = env.step(action)
            next_state, reward, done, *_ = result  # Adjusted unpacking

            delta = reward + gamma * V[next_state] - V[state]
            eligibility_trace[state] += 1

            V += alpha * delta * eligibility_trace
            eligibility_trace *= gamma * lambtha

            if done:
                break
            state = next_state[0] if isinstance(next_state, tuple) else next_state

    return V
