# Graph Search
Depth First Algorithm:
https://www.youtube.com/watch?v=0_ZzqX5bpyA

Breadth First Algorithm:
https://www.youtube.com/watch?v=WiasVg9M81I

## Advantages of Depth First Search:

    Memory requirement is only linear with respect to the search graph. This is in contrast with breadth-first search which requires more space. The reason is that the algorithm only needs to store a stack of nodes on the path from the root to the current node.
    The time complexity of a depth-first Search to depth d and branching factor b (the number of children at each node, the outdegree) is O(bd) since it generates the same set of nodes as breadth-first search, but simply in a different order. Thus practically depth-first search is time-limited rather than space-limited.
     If depth-first search finds solution without exploring much in a path then the time and space it takes will be very less.
    DFS requires less memory since only the nodes on the current path are stored. By chance DFS may find a solution without examining much of the search space at all.

## Disadvantages of Depth First Search:

    The disadvantage of Depth-First Search is that there is a possibility that it may down the left-most path forever. Even a finite graph can generate an infinite tre One solution to this problem is to impose a cutoff depth on the search. Although ideal cutoff is the solution depth d and this value is rarely known in advance of actually solving the problem. If the chosen cutoff depth is less than d, the algorithm will fail to find a solution, whereas if the cutoff depth is greater than d, a large price is paid in execution time, and the first solution found may not be an optimal one.
     Depth-First Search is not guaranteed to find the solution.
     And there is no guarantee to find a minimal solution, if more than one solution.


## Advantages of Breadth First Search:

    BFS will never get trapped exploring the useful path forever.
    If there is a solution, BFS will definitely find it.
    If there is more than one solution then BFS can find the minimal one that requires less number of steps.
    Low storage requirement – linear with depth.
    Easily programmable.

## Disadvantages of Breadth First Search:

The main drawback of BFS is its memory requirement. Since each level of the graph must be saved in order to generate the next level and the amount of memory is proportional to the number of nodes stored the space complexity of BFS is O(bd ), where b is the branching factor(the number of children at each node, the outdegree) and d is the depth. As a result, BFS is severely space-bound in practice so will exhaust the memory available on typical computers in a matter of minutes.
