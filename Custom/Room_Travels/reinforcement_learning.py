"""

Custom made reinforcement learning algorithm

"""

import random

class ReinforcementAgent:
    def __init__(self, states):
        self.states = states
        self.currentRoom = self.setStartingPoint()
        self.starting_point = self.setStartingPoint()
        self.steps_taken = 0

        self.gamma = 0.8 # Learning Curve

    def setStartingPoint(self):
        for state in self.states:
            if state.is_start == True:
                return state

    def chooseRoom(self):
        max_path = None
        max_q_value = 0
        list_paths = list(self.currentRoom.paths.values())
        num = random.randrange(0, len(list_paths))

        next_max_q = 0

        for k, path in self.currentRoom.paths.iteritems():
            if path.q_value > max_q_value:
                #print k, path.room_one.room_name, path.q_value
                max_path = path
                max_q_value = max_path.q_value

        if max_q_value == 0:
            max_path = list_paths[num]


        next_room_paths = list(max_path.room_two.paths.values())
        for path in next_room_paths:
            if path.q_value > next_max_q:
                next_max_q = path.q_value

        # print "Next Room: ", max_path.room_two.room_name
        # print next_max_q
        # print max_path.path_weight
        max_path.q_value = self.qLearning(max_path.path_weight, next_max_q)
        self.currentRoom.paths[max_path.room_two.room_name].q_value = max_path.q_value
        self.steps_taken += 1
        self.currentRoom = max_path.room_two
        # print "Current Room: ", self.currentRoom.room_name

    def sanityCheck(self):
        for state in self.states:
            print "In State: ", state.room_name
            for k, v in state.paths.iteritems():
                print k, v.q_value

    def isFinish(self):
        if self.currentRoom.is_goal:
            print "GOOAAAAAL"
            print "Steps Taken: ", self.steps_taken
            self.currentRoom = self.setStartingPoint()
            self.steps_taken = 0
            # self.sanityCheck()

    def qLearning(self, reward_weight, q_value):
        return reward_weight + self.gamma * q_value


