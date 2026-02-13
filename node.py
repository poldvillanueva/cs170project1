class Node:                                         
    def __init__(self, state, g, h, parent):        #initialize node                      
        self.state = state 
        self.g = g
        self.h = h; 
        self.parent = parent
        self.f = g + h                              #A* est cost

    def __lt__(self, other):                        #priority queue comparison 
        return self.f < other.f



