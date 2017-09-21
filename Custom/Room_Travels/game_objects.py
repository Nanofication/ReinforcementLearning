"""

Room Class

Each room has a name and a number of doors

The room can have a win state or a none win state

Each room has a certain number of paths to other rooms

"""

class Room:
    def __init__(self, room_name, num_doors, is_goal = False):
        self.room_name = room_name
        self.num_doors = num_doors
        self.is_goal = is_goal
        self.paths = []


class Path:
    def __init__(self, room_one, room_two, weight):
        self.room_one = room_one
        self.room_two = room_two
