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
