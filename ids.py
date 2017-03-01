# ids.py
# Implemenatation of Iterative Deepening Search
# Aviva Blonder

import time
import searchtree


class IDS():

    def __init__(self, model):
        """ Initialize the algorithm with a model to search through """
        self.model = model


    def search(self):
         """ Iterative Deepending Search algorithm to find a path to a goal state from the start state in the provided model (workflow modified from BFS) """

         # start the timer
         stime = time.process_time()
         # create a search tree to hold all explored nodes, starting with the start state
         root = searchtree.Stree(self.model.startState(), 0)

         # increase depth until a solution is found or it runs out of nodes
         for depth in range(1, len(self.model.net.nodes)):
             # initialize list of states that have been explored during the search and the depths at which they have been found
             self.explored = {}
             # start the recursive search on the start state and grab the result
             result = self.rsearch(root, depth)
             # if the result isn't none, it's a success!
             if result:
                 # stop the timer
                 etime = time.process_time()
                 print("SUCCESS!")
                 print("Runtime: " + str(etime-stime) + " seconds")
                 print("Number of nodes explored: " + str(len(self.explored)))
                 print("Path length: " + str(depth))
                 print("Path cost: " + str(result.cost))
                 #  and then return to quit
                 return

         # if it gets to this point, it's gone through every node in the problem and no goal has been found, indicating that there is no way to get from the start state to the goal
         print("Goal not found!")


    def rsearch(self, node, depth):
        """ Recursive search method that will do the heavy lifting in the search algorithm """

        # add the current node to the explored set
        self.explored[node.state] = node.path
        # if the current node is a goal state, just stop there
        if self.model.goal(node.state):
            return node
        # if the depth is 0, that means the cutoff has been reached and it's time to stop
        if depth == 0:
            return None
        # otherwise, loop through all of this node's children and see if any of them get to a goal state
        for act in self.model.actions(node.state):
            # save the result
            result = self.model.result(node.state, act)
            # if the action has not been explored yet or is higher up, recurse on it
            if result not in self.explored or self.explored[result] > node.path + 1:
                outcome = self.rsearch(node.expand(result, self.model.cost(node.state, act)), depth-1)
                # if the outcome isn't None, return it
                if outcome:
                    return outcome
        # if no path has been found and returned, the cutoff has been reached on all chidlren and it's time to admit defeat
        return None
        
