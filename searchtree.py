# searchtree.py
# Helper search tree class to hold the nodes that have been explored so far in the search algorithms
# Aviva Blonder

import copy

class Stree():

    def __init__(self, state, cost, path = 0, heuristic = 0):
        """ Creates a new Stree object given a state, the cumulative cost and length of the path to get there, and a list of states that have been explored already on this path. """
        self.state = state
        self.cost = cost
        # the length of the path so far
        self.path = path
        # empty list of children
        self.children = []
        # heuristic value for comparison in the priority heap in A*
        self.heuristic = heuristic


    def expand(self, action, cost, heuristic = 0):
        """ Creates a child node for a given action from this state and returns it. """

        # create a new leaf with the designated action, cost, and heuristic
        new = Stree(action, self.cost+cost, self.path+1, self.cost+heuristic)
        # add the leaf to the list of children
        self.children.append(new)
        # return the new child
        return new


    def __lt__(self, other):
        """ Enables two trees to be compared for sorting in the priority heap for A* """
        return self.heuristic < other.heuristic
