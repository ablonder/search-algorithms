# What is the Best Way to Search?

I implemented and evaluated 4 search algorithms: Breadth First Search, A*, Iterative Deepening Search, and a smarter Iterative Deepening Search that was modified to make sure it didn't repeatedly re-do the same work.

<table>
  <tr><td rowspan=2></td><th colspan=4>Network 1</th><th colspan=4>Network 2</th><th colspan=3>Network 3</th></tr>
  <tr><th>BFS</th><th>A*</th><th>IDS</th><th>Modified IDS</th><th>BFS</th><th>A*</th><th>IDS</th><th>Modified IDS</th><th>BFS</th><th>A*</th><th>IDS</th></tr>
  <tr><th>Runtime (seconds)</th><td>0.0393</td><td>0.0043</td><td>0.1553</td><td>0.0859</td><td>4.5424</td><td>0.0949</td><td>23.2790</td><td>7.6172</td><td>1590.1788</td><td>49.0080</td><td rowspan=4>Exceeds maximum recursive depth.</td></tr>
  <tr><th># nodes explored</th><td>380</td><td>51</td><td>284</td><td>341</td><td>4105</td><td>448</td><td>1556</td><td>4105</td><td>39525</td><td>8689</td></tr>
  <tr><th>Path length</th><td>10</td><td>10</td><td>35</td><td>10</td><td>27</td><td>28</td><td>140</td><td>27</td><td>80</td><td>89</td></tr>
  <tr><th>Path cost</th><td>4.5913</td><td>4.4484</td><td>9.4628</td><td>4.5913</td><td>4.5000</td><td>4.2137</td><td>14.1892</td><td>4.500</td><td>6.4321</td><td>5.9150</td></tr>
</table>

Based on the results above, A* was clearly the best of the three algorithms I implemented. I decided to use Euclidian distance as my heuristic because the path costs were based on distance between nodes, so the cost to get from a given node to a goal state had to be at least the distance between the node and the nearest goal. That means I used an admissable heuristic, so the algorithm should always find the optimal path. The results of running the three algorithms on the networks provided indicate that this is in fact the case. On all three networks, A* found the path with the lowest cost and furthermore did it faster and by exploring fewer nodes than Breadth Firdst Search or Iterative Deepening Search.

My IDS implementation performed the worst of the three algorithms and wasn't even able to find a path to a goal state in network 3 without exceeding the maximum recursive depth. I believe it found such bad paths in networks 1 and 2 becuase states were added to the explored set as it expanded them. Because it performed depth first search, it was possible for a state to be expanded far down on one path before it could be encountered less far down on a path that just happened to be expanded later. This also explains why it found such expensive paths. To improve the algorithm's performance, I modified the explored set to keep track of the depth at which a state was found and explore it again only if it appeared higher up. That way, I was able to leave open the opportunity to find a shorter, less expensive path through a state, even if it was encountered later. As the results from "IDS with modified explored set" show, it resulted in paths with the same length and cost as BFS, though it took longer to find them and I was unable to successfuly run it on network 3 becuase it crashed my computer.

Reflection: Implementing the search algorithms was surprisingly easy, the code is pretty short and not terribly complicated. Debugging was a little more complicated. Initially I tried keeping a recursive explored set for each path, which caused BFS to take so long and use so much space that my computer froze whenever I ran it. It took me some time to realize that was the problem, so I was worried about infinite loops for a little while. I also had a bit of trouble with A*, which was returning worse paths than BFS because I forgot to add the cost of the path so far to the heuristic. I also had some difficulty with IDS crashing as described above.
