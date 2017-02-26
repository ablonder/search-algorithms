# searchtree.py
# Helper search tree class to hold the nodes that have been explored so far in the search algorithms
# Aviva Blonder

import copy

class Stree():

    def __init__(self, state, cost, path = 0):
        """ Creates a new Stree object given a state, the cumulative cost and length of the path to get there, and a list of states that have been explored already on this path. """
        self.state = state
        self.cost = cost
        # the length of the path so far
        self.path = path
        # empty list of children
        self.children = []

    def expand(self, action, cost):
        """ Creates a child node for a given action from this state and returns it. """

        # create a new leaf with the designated action and cost
        new = Stree(action, self.cost+cost, self.path+1)
        # add the leaf to the list of children
        self.children.append(new)
        # return the new child
        return new
