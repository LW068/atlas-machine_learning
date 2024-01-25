#!/usr/bin/env python3
import numpy as np
import gym


def train(env, nb_episodes, alpha=0.000045, gamma=0.98, show_result=False):
    """
    Implement a full trainign.
    
    :param env: initial environment
    :param nb_episodes: number of episodes used for training
    :param alpha: the learning rate
    :param gamma: the discount factor
    :return: all values of the score (sum of all rewards during one episode loop)
    """
    weight = np.random.rand(4, 2)
    scores = []

    for episode in range(nb_episodes):
        state = env.reset()
        state = np.array([state])
        episode_rewards = 0

        while True:
            action, grad = policy_gradient(state, weight)
            state, reward, done, _ = env.step(action)
            state = np.array([state])
            weight += alpha * grad * reward
            episode_rewards += reward

            if done:
                break

        scores.append(episode_rewards)

        if show_result and episode % 1000 == 0:
            print(f"Episode: {episode+1}, Score: {episode_rewards}")
            env.render()

        print(f"Episode: {episode+1}, Score: {episode_rewards}", end="\r", flush=True)

    return scores


def policy(matrix, weight):
    """
    Compute the policy from a given state matrix and weight matrix.

    :param matrix: numpy.ndarray - The state matrix
    :param weight: numpy.ndarray - The weight matrix
    :return: The computed policy as a probability distribution over actions
    """
    z = np.dot(matrix, weight)
    exp = np.exp(z)
    return exp / np.sum(exp, axis=1, keepdims=True)


def policy_gradient(state, weight):
    """
    Compute the Monte-Carlo policy gradient.
    
    :param state: matrix representing the current observation of the environment
    :param weight: matrix of random weight
    :return: the action and the gradient (in this order)
    """
    probs = policy(state, weight)
    action = np.random.choice(len(probs[0]), p=probs[0])

    # constructing the softmax gradient
    softmax_grad = np.diag(probs.ravel()) - np.outer(probs, probs)
    selected_action_grad = softmax_grad[action]

    # computing the gradient of the log probability
    log_prob_grad = selected_action_grad / probs[0, action]

    # Fginal gradient with respect to weights
    gradient = np.dot(state.T, log_prob_grad.reshape(1, -1))

    return action, gradient