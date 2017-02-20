"""
The BFS class represents an objet capable of using Breadth First Search to find a
path to goal state from a start state in a given Problem

<Name>
<Date>
"""

import time

class BFS():
    """
    Creates a new BFS object

    model: a Problem model of the environment
    """
    def __init__(self, model):
        # save the params
        self.model = model

    """
    Searches for a path from the start state to a goal state using the
    Problem model given to the constructor
    """
    def search(self):
        pass # implement this!
