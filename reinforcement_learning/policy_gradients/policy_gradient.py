#!/usr/bin/env python3
"""POLICY GRADIENT!!!!"""
import numpy as np


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