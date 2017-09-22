from game_objects import Room, Path

if __name__ == "__main__":
    rooms = []

    a = Room("A", 1, is_start=True)
    b = Room("B", 1)
    c = Room("C", 1)
    d = Room("D", 1)
    e = Room("E", 1)
    f = Room("F", 1, is_goal=True)

    # Connect Rooms together
    a.add_path(e)

    e.add_path(a)
    e.add_path(f)
    e.add_path(d)

    d.add_path(e)
    d.add_path(c)
    d.add_path(b)

    c.add_path(d)

    b.add_path(d)
    b.add_path(f)

    f.add_path(b)
    f.add_path(e)

    rooms = [a,b,c,d,e,f]

    # for room in rooms:
    #     print room.room_name
    #     print room.paths

    #### Reinforcement Learning