from game_objects import Room
from reinforcement_learning import ReinforcementAgent

if __name__ == "__main__":
    rooms = []

    a = Room(0, is_start=True)
    b = Room(1)
    c = Room(2)
    d = Room(3)
    e = Room(4)
    f = Room(5)
    g = Room(6)
    h = Room(7)
    i = Room(8)
    j = Room(9, is_goal=True)

    # Connect Rooms together
    a.add_path(e)
    a.add_path(c)
    a.add_path(d)

    e.add_path(a)
    e.add_path(c)
    e.add_path(d)

    d.add_path(e)
    d.add_path(c)
    d.add_path(b)

    c.add_path(d)
    c.add_path(i)

    b.add_path(d)
    b.add_path(h)

    f.add_path(b)
    f.add_path(e)

    g.add_path(j, 100)
    g.add_path(h)
    g.add_path(a)

    h.add_path(a)
    h.add_path(b)
    h.add_path(c)
    h.add_path(e)


    i.add_path(b)
    i.add_path(c)
    i.add_path(j, 100)
    i.add_path(h)

    rooms = [a,b,c,d,e,f, g, h, i, j]

    a = ReinforcementAgent(rooms)
    print a.states
    count = 0
    a.sanityCheck()
    while count < 10000:
        a.chooseRoom()
        a.isFinish()
        count+= 1


    #### Reinforcement Learning
