"""
The AStar class represents an object capable of using A* Search to find a
path to goal state from a start state in a given Problem

<Name>
<Date>
"""

import time

class AStar():
    """
    Creates a new AStar object

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
