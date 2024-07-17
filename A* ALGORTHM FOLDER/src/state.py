class State:

    # state constructor
    def __init__(self, size, start, goal):
        self.size = size
        self.start = start
        self.goal = goal
        self.f = {}
        self.h = None
        self.g = set()
        self.closed_list = set()
        self.distance = None
    
    def F(self):
        return self.f

    def H(self):
        return self.h

    def G(self):
        return self.g

    def closedList(self):
        return self.close_list
    
    def manhattan(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    