"""

Room Class

Each room has a name and a number of doors

The room can have a win state or a none win state

Each room has a certain number of paths to other rooms

"""

class GameManager:
    def __init__(self):
        self.rooms = []
        self.paths = []

    def add_room(self, room):
        if room in self.rooms:
            print "Room already exists"
        else:
            self.rooms.append(room)

    def add_path(self, path):
        if path in self.paths:
            print "Path already exists"
        else:
            self.paths.append(path)

class Room:
    def __init__(self, room_name, num_doors, is_start = False, is_goal = False):
        self.room_name = room_name
        self.num_doors = num_doors
        self.is_start = is_start
        self.is_goal = is_goal
        self.paths = []

    def add_path(self, path):
        """
        Add a path to another room with this room set as the origin
        :param path: Path to another room
        """
        if path.room_one.room_name != self.room_name:
            print "Path's first room is not this room. Not added"
        else:
            self.paths.append(path)


class Path:
    def __init__(self, room_one, room_two, path_weight):
        self.room_one = room_one
        self.room_two = room_two
        self.path_weight = path_weight
