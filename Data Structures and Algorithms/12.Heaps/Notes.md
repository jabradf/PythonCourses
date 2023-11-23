* A max-heap tracks the maximum element as the element at index `1` within an internal Python list.
* Max-heaps must maintain the heap property that the parent values must be greater than their children.
* When adding elements, we use `.heapify_up()` to compare the new element with its parent; if it violates the heap property, then we must swap the two values.

Heapsort is efficient wiht O(log(n)).

# Heap Sort
* A heapsort algorithm uses the heap data structure to organize data.
* The first step to implement heapsort is to place the data inside a heap.
* While the heap has more than one element, extract the largest value in the heap by swapping it with the right-most child and then removing it.
* After we swap the root value and the last value, we must restructure the heap until every parent has a larger value than their children again.
  