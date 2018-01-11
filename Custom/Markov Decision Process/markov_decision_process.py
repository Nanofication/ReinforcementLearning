"""
Markov Decision Process: MDP

Includes:
1. Agent
2. Decision Making Process

Steps:
1. Set of Possible States: S = {s0, s1, s2 ..., sm}
2. Initial State: s0
3. Set of possible Actions: A = {a0, a1, a2,.... an}
4. Transition Model: T(s, a, s') - probability of reaching the state s' if action a is done in state s
5. Reward Function: R(s)

Objective: The agent has to maximize the rewards it acquires while traveling through the states.
The agent must find a policy which returns the action with the highest reward. (An optimal policy)

"""

"""
Scenario: You are on a very hot beach starting at s0 (1,1)
WORLD: 4 x 3 beach. Trash can at (2,2) Broken glass at (4,2) -1 Reward
and cool water at (4,3) +1 Reward

Each step, you have stochastic factor where you may change your mind and go to another path.
You will take the path you want to go 80% of time, 10% of time you go right or 10% go to left

Hit the trash can, you go back.

1. Discrete Time and Space
2. Fully Observable - Always know which state you are in
3. Infinite Horizon - No time limit
4. Known Transition Model

"""

import numpy as np

def getStateUtility(v, T, u, reward, gamma):
    """
    Bellman Equation:

    U(s) = R(s) + gamma * max action SUM [for all s' (T(s,a,s')Utility(s')]

    in code format

    :param v: The state vector. Where the person is in this world
    :param T: Transition Matrix
    :param u: Utility Vector
    :param reward: Reward for the state
    :param gamma: Discount Factor
    :return: The utlity of the state
    """
    actions = np.zeros(4)
    for action in range(4):
        actions[action] = np.sum(np.multiply(u, np.dot(v, T[:,:,action])))
    return reward + gamma * np.max(actions)

if __name__ == "__main__":
    # Person starts at (1,1)
    v = np.array([[0.0, 0.0, 0.0, 0.0,
                   0.0, 0.0, 0.0, 0.0,
                   1.0, 0.0, 0.0, 0.0]])
    # Transition Matrix is 12 Starting States x 12 Next States x 4 Actions
    T = np.load("T.npy")

    # Utility Vector
    u = np.array([0.812, 0.868, 0.918, 1.0,
                  0.762, 0.0, 0.660, -1.0,
                  0.705, 0.655, 0.611, 0.388]) # This is arbitrarily set *MAGIC*

    reward = -0.04

    gamma = 1.0

    # Find utility of state (1,1)
    utility_1 = getStateUtility(v, T, u, reward, gamma)
    print "Utility of state (1,1): %s" % str(utility_1)

