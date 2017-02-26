"""
The BFS class represents an objet capable of using Breadth First Search to find a
path to goal state from a start state in a given Problem

Aviva Blonder
March 1st, 2017
"""

import time
import searchtree
from queue import Queue

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
        # start the timer
        stime = time.process_time()
        # create a search tree to hold all explored nodes, starting with the start state
        root = searchtree.Stree(self.model.startState(), 0)
        # create a queue to hold the list of nodes to explore
        frontier = Queue()
        # add the start state to the fronteir set
        frontier.put_nowait(root)
        # list of state that have been explored during the search
        explored = []
        
        # expand the next node in the fronteir set until it is empty (or a goal has been reached)
        while not frontier.empty():
            # pop the next state from the frontier set
            n = frontier.get_nowait()
            # loop through the possible actions that can be taken from that state and expand them
            for act in self.model.actions(n.state):
                # save the result
                result = self.model.result(n.state, act)
                # if the action has not been explored yet
                if result not in explored:
                    # add it to the list of states that have been explored so far
                    explored.append(result)
                    # expand that child
                    c = n.expand(result, self.model.cost(n.state, act))
                    # if act is a goal state, print out the amount of time it took, number of nodes explored, the length of the path to the goal, and its cost
                    if self.model.goal(result):
                        # stop the timer
                        etime = time.process_time()
                        print("SUCCESS!")
                        print("Runtime: " + str(etime-stime) + " seconds")
                        print("Number of nodes explored: " + str(len(explored)))
                        print("Path length: " + str(c.path))
                        print("Path cost: " + str(c.cost))
                        #  and then return to quit
                        return
                    # otherwise, add it to the frontier set and keep going
                    frontier.put_nowait(c)

        # if it gets to this point, the frontier is empty and no goal has been found, indicating that there is no way to get from the start state to the goal
        print("Goal not found!")
