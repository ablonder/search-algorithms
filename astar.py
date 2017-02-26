"""
The AStar class represents an object capable of using A* Search to find a
path to goal state from a start state in a given Problem

Aviva Blonder
March 1st, 2017
"""

import time
from heapq import *
import searchtree

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
        # start the timer
        stime = time.process_time()
        # create a search tree to hold all explored nodes, starting with the start state
        root = searchtree.Stree(self.model.startState(), 0, heuristic=self.disttogoal(self.model.startState()))
        # create a list to hold the fronteir set, which will be a priority heap
        frontier = []
        # add the start state and the estimated distance to the nearest goal (my heuristic) to the frontier set
        heappush(frontier, root)
        # list of state that have been explored during the search
        explored = []
        
        # expand the next node in the fronteir set until it is empty (or a goal has been reached)
        while len(frontier) > 0:
            # pop the next state from the frontier set
            n = heappop(frontier)
            # loop through the possible actions that can be taken from that state and expand them
            for act in self.model.actions(n.state):
                # save the result
                result = self.model.result(n.state, act)
                # if the action has not been explored yet
                if result not in explored:
                    # add it to the list of states that have been explored so far
                    explored.append(result)
                    # expand that child
                    c = n.expand(result, self.model.cost(n.state, act), heuristic=self.disttogoal(result) + abs(n.state[0]-result[0]) + abs(n.state[1]-result[0]))
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
                    # otherwise, calculate the total heuristic distance, add it to the frontier set and keep going
                    heappush(frontier, c)

        # if it gets to this point, the frontier is empty and no goal has been found, indicating that there is no way to get from the start state to the goal
        print("Goal not found!")

    def disttogoal(self, state):
        """ Calculates the distance between a given state and the nearest goal """

        # will hold the distance to the nearest goal
        bestdist = None
        # loop through all the possible goal states
        for goal in self.model.goalStates():
            # calculate Manhattan distance (because it's largest)
            dist = abs(state[0]-goal[0]) + abs(state[1]-goal[1])
            # if no nearest goal has been found yet, or this is closer
            if not bestdist or dist < bestdist:
                # make this the best
                bestdist = dist
        # return the distance to the nearest goal
        return bestdist
