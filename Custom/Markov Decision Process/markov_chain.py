"""
Markov Chain Introduction

1. Set of Possible States: S = {s0, s1, s2 ..., sm}
2. Initial State: s0
3. Transition Model: T = (s,a,s') Probability go to State s' from state s using action a

Assumptions:
Given the present, the future is conditionally independent of the past.

References: https://mpatacchiola.github.io/blog/2016/12/09/dissecting-reinforcement-learning.html
Georgia Tech Reinforcement Learning
"""

import numpy as np

"""
Transition Matrix T
0.9, 0.1
0.5, 0.5

When process is in s0. IT will stay there 90% of the time and it can move to s1 10% of the time
When process is in s1. It will move to s0 50% of  the time and stay in s1 50% of the time

"""
T = np.array([[0.9, 0.1],[0.5, 0.5]])

def getTransitionMatrix(transition_matrix, steps):
    """
    Calculate the distribution of probabilities of entering a specific state after k iterations.
    This is represented as a matrix after taking the initial distribution (matrix) of transition probabilities
    to the power of k-steps
    :param transition_matrix: The Transition Matrix of a Markov Chain. A matrix with the probabilities of entering
     different states.
    :param steps: The k-step, number of steps, that the process underwent
    :return: The distribution of probabilities after going through k steps:
     The distribution of probabilities matrix after undergoing k steps of iterations
    """
    return np.linalg.matrix_power(transition_matrix, steps)

def getStateDistribution(vector_distribution, transition_matrix):
    """
    Calculate the probability of being in a specific state after k iterations
    :param vector_distribution: Matrix representation of a vector environment with where the agent begins labeled as 1.0
    or 0.5 if unsure. Be sure that all the probabilities add up to 1.0. I.E. (1.0, 0.0, 0.0....) or (0.5, 0.25, 0.25,..)
    :param transition_matrix: Matrix representation of probabilities of transitions between states
    :return: The probability of being in a specific state after k iterations.
    """
    return np.dot(vector_distribution, transition_matrix)


if __name__ == "__main__":
    # Obtaining T after 1 Step
    print "T after 1 step: ", getTransitionMatrix(T, 1)

    # Obtaining T after 3 Steps
    print "T after 3 steps: ", getTransitionMatrix(T, 3)

    # Obtaining T after 50 Steps
    print "T after 50 steps: ", getTransitionMatrix(T, 50)

    # Obtaining T after 100 Steps
    print "T after 100 steps: ", getTransitionMatrix(T, 100)

    # State Distributions
    v = np.array([[1.0, 0.0]])

    print "Distribution after 1 Step: ", np.dot(v, getTransitionMatrix(T, 1))
    print "Distribution after 3 Step: ", np.dot(v, getTransitionMatrix(T, 3))
    print "Distribution after 50 Step: ", np.dot(v, getTransitionMatrix(T, 50))
    print "Distribution after 100 Step: ", np.dot(v, getTransitionMatrix(T, 100))

    # NOTE: More steps takes us closer to equilibrium
    