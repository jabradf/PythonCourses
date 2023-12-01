# A* Review
* The A* algorithm is a greedy graph search algorithm that optimizes looking for a target vertex.
* A* is a modification of Dijkstra’s done by adding the estimated distance of each vertex to the goal vertex when searching.
* We can modify Dijkstra’s and turn it into A* by changing the following:
  * Adding a target for the search.
  * Gathering possible optimal paths and identify a single shortest path.
  * Implementing a heuristic that determines the likely distance remaining.
* The runtime of A* is `O(b^d)` where `b` is the branching factor of the graph and `d` is the depth of the goal vertex from the start vertex.
* A* is an introductory glimpse into artificial intelligence.