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

def runArbitraryUtilities():
    # Person starts at (1,1)
    v = np.array([[0.0, 0.0, 0.0, 0.0,
                   0.0, 0.0, 0.0, 0.0,
                   1.0, 0.0, 0.0, 0.0]])
    # Transition Matrix is 12 Starting States x 12 Next States x 4 Actions
    T = np.load("T.npy")

    # Utility Vector
    u = np.array([0.812, 0.868, 0.918, 1.0,
                  0.762, 0.0, 0.660, -1.0,
                  0.705, 0.655, 0.611, 0.388])  # This is arbitrarily set *MAGIC*

    reward = -0.04

    gamma = 1.0

    # Find utility of state (1,1)
    utility_1 = getStateUtility(v, T, u, reward, gamma)
    print "Utility of state (1,1): %s" % str(utility_1)

def valueIterationAlgorithm(debug=False):
    """
    Find utilities of the state until Utilities differences meet equilibrium
    Equation for reaching equilibrium state:

    ||U(k+1) - U(k)|| < epsilon * ((1 - gamma)/gamma)

    epsilon = stopping criteria. Small Value
    """
    total_states = 12
    gamma = 0.999 # Discount factor
    iteration = 0 # Iteration counter
    epsilon = 0.01 # Stopping criteria small value

    graph_list = list() # List containing the data for each iteration

    # Transition Matrix is 12 Starting States x 12 Next States x 4 Actions
    T = np.load("T.npy")

    # Reward Vector
    r = np.array([-0.04, -0.04, -0.04, +1.0,
                  -0.04, 0.0, -0.04, -1.0,
                  -0.04, -0.04, -0.04, -0.04])

    # Utility Vectors (Arbitrary Utilities for each state. Usually zero)
    u_1 = np.array([0.0, 0.0, 0.0, 0.0,
                  0.0, 0.0, 0.0, 0.0,
                  0.0, 0.0, 0.0, 0.0])

    # Once we reach equilibrium, we have hte utility values we were looking for to be used to estimate which
    # is the best move for each state

    while True:
        delta = 0
        u = u_1.copy()
        iteration += 1
        graph_list.append(u)

        for s in range(total_states):
            reward = r[s]
            v = np.zeros((1, total_states))
            v[0,s] = 1.0
            u_1[s] = getStateUtility(v, T, u, reward, gamma)
            delta = max(delta, np.abs(u_1[s] - u[s]))
        if debug:
            print "Iterations: " + str(iteration)
            print "Delta: " + str(delta)
            print "Gamma: " + str(gamma)
            print "Epsilon: " + str(epsilon)
            print "============================="
            print u[0:4]
            print u[4:8]
            print u[8:12]
            print "============================="
        if delta < epsilon * (1 - gamma) / gamma:
            print "======= FINAL RESULT ========"
            print "Iterations: " + str(iteration)
            print "Delta: " + str(delta)
            print "Gamma: " + str(gamma)
            print "Epsilon: " + str(epsilon)
            print "============================="
            print u[0:4]
            print u[4:8]
            print u[8:12]
            print "============================="
            break

def returnPolicyEvaluation(policy, utilities, reward, transition_matrix, gamma):
    """
    Return the policy utility
    :param p: policy vector
    :param u: utility vector
    :param r: reward vector
    :param transition_matrix: List of matrices of probabilities for going from 1 state to another
    :param gamma: The discount factor
    :return: The utility vector
    """
    for s in range(12):
        if not np.isnan(policy[s]): # If the agent took an action
            v = np.zeros((1,12))
            v[0,s] = 1.0
            action = int(policy[s])
            utilities[s] = reward[s] + gamma * np.sum(np.multiply(utilities, np.dot(v, transition_matrix[:,:,action])))
    return utilities

def returnExpectedAction(utilities, transition_matrix, starting_vector):
    """
    Return the expected action.

    Returns an action based on the expected utility of performing action in state s,
    according to transition_matrix and utilities. This action is the one that
    maximize the expected utility.
    :param utilities: Utility Vector
    :param transition_matrix: Transition Matrix
    :param starting_vector: Starting Vector for agent
    :return: Expection action (integer)
    """
    actions_array = np.zeros(4)
    for action in range(4):
        # Expected utility of performing action a in state s, according to the transition matrix and utilities vector
        actions_array[action] = np.sum(np.multiply(utilities, np.dot(starting_vector, transition_matrix[:,:,action])))
    return np.argmax(actions_array)

def printPolicy(policy, shape):
    """
    Printing The Utility

    Print the policy actions using symbols:
    ^, V, <, > up, down, left, right
    * terminal states
    # obstacles
    :param policy:
    :param shape:
    :return:
    """
    counter = 0
    policy_string = ""
    for row in range(shape[0]):
        for col in range(shape[1]):
            if policy[counter] == -1: policy_string += " * "
            elif policy[counter] == 0: policy_string += " ^ "
            elif policy[counter] == 1: policy_string += " < "
            elif policy[counter] == 2: policy_string += " V "
            elif policy[counter] == 3: policy_string += " > "
            elif np.isnan(policy[counter]): policy_string += " # "
            counter += 1
        policy_string += '\n'
    print policy_string

def policyIterationAlgorithm():
    """
    We estimate the utility of each state.
    This is guaranteed to converge. The policy and its utility function are the optimal ones
    1. Define policy, it can be random.
    2. We can use the simplified version of Bellman (No Max)
    Each iteration generates a better policy
    :return:
    """
    gamma = 0.999
    epsilon = 0.0001
    iteration = 0
    transition_matrix = np.load("T.npy")

    # Generate the first policy randomly (Like Neural Networks) Random actions
    # NaN = Nothing, -1 = Terminal, 0 = Up, 1 = Left, 2 = Down, 3 = Right
    policy = np.random.randint(0, 4, size=(12)).astype(np.float32)
    policy[5] = np.NaN
    policy[3] = policy[7] = -1

    # Utility Vectors
    utility_vector = np.array([0.0, 0.0, 0.0, 0.0,
              0.0, 0.0, 0.0, 0.0,
              0.0, 0.0, 0.0, 0.0])

    # Reward Vector
    reward_vector = np.array([-0.04, -0.04, -0.04, +1.0,
                  -0.04, 0.0, -0.04, -1.0,
                  -0.04, -0.04, -0.04, -0.04])

    while True:
        iteration += 1
        # 1. Policy Evaluation
        u_0 = utility_vector.copy()
        utility_vector = returnPolicyEvaluation(policy, utility_vector, reward_vector, transition_matrix, gamma)

        #Stopping criteria
        delta = np.absolute(u_0 - utility_vector).max()
        if delta < epsilon * (1 - gamma)/gamma: break
        for s in range(12):
            if not np.isnan(policy[s]) and not policy[s] == -1:
                v = np.zeros((1, 12))
                v[0,s] = 1.0
                # 2. Policy improvement
                action = returnExpectedAction(utility_vector, transition_matrix, v)
                if action != policy[s]: policy[s] = action
        printPolicy(policy, shape=(3,4))

    print("=================== FINAL RESULT ==================")
    print("Iterations: " + str(iteration))
    print("Delta: " + str(delta))
    print("Gamma: " + str(gamma))
    print("Epsilon: " + str(epsilon))
    print("===================================================")
    print(utility_vector[0:4])
    print(utility_vector[4:8])
    print(utility_vector[8:12])
    print("===================================================")
    printPolicy(policy, shape=(3, 4))
    print("===================================================")

if __name__ == "__main__":
    # runArbitraryUtilities()
    # valueIterationAlgorithm(True)
    # T = np.load("T.npy")
    policyIterationAlgorithm()