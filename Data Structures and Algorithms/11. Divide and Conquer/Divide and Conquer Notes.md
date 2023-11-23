* Divide-and-conquer is a strategy that solves a large problem by recursively breaking it down into smaller subproblems until they can be solved directly.
* Divide-and-conquer works in three steps: divide, conquer, and combine.
* The time complexity of a divide-and-conquer algorithm is determined by the cost of division (log(n)) and the cost of solving the subproblems.
* Advantages: 
  * Simplify large and complex problems by breaking them down into subproblems.
  * More efficient than brute force approaches.
  * Can access memory caches efficiently.
* Disadvantages:
* Risk of stack overflow due to the recursion stack.
* Cannot avoid evaluating the same subproblem repeatedly.

For merge sort, division takes `O(log(n))` time, and combining the sorted sublists takes `O(n)` time. Therefore, merge sort has a big-O runtime of O(nlog(n)).