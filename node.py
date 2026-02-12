class Node: 
    def __init__(self, state, g, h, parent):
        self.state = state 
        self.g = g
        self.h = h; 
        self.parent = parent
        self.f = g + h

    def __lt__(self, other):
        return self.f < other.f



