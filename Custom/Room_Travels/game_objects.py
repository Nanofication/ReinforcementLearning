"""

Room Class

Each room has a name and a number of doors

The room can have a win state or a none win state

Each room has a certain number of paths to other rooms

"""

class Room:
    def __init__(self, room_name, is_start = False, is_goal = False):
        self.room_name = room_name
        self.is_start = is_start
        self.is_goal = is_goal
        self.paths = {}

    def add_path(self, room, path_weight = 0):
        """
        Add a path to another room with this room set as the origin
        :param path: Path to another room
        """
        if room == self:
            print "You cannot add a path to yourself. Not added"
        else:
            path = Path(self,room, path_weight)
            self.paths[path.path_name] = path


class Path:
    def __init__(self, room_one, room_two, path_weight = 0):
        self.room_one = room_one
        self.room_two = room_two
        self.path_weight = path_weight

        self.path_name = room_two.room_name
        self.q_value = 0