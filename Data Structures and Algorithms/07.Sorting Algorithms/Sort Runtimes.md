# Sort Runtimes
A brief overview of the time and space complexities of our sorting algorithms.

## Sorting Algorithm Runtimes
There are many different sorting algorithms, but the three we focused on were bubble sort, merge sort, and quicksort. They all have pros and cons when it comes to their efficiency. Let’s take a quick dive into each one!

## Asymptotic Notation Refresher
As a reminder, when we need a more general way to gauge a program’s runtime, we use asymptotic notation.

Instead of timing a program, through asymptotic notation, we can calculate a program’s runtime by looking at how many instructions the computer has to perform based on the size of the program’s input: n. We also use this when calculating the amount of space a certain program will need.

## Bubble Sort
Bubble sort is an introductory sorting algorithm that iterates through a list and compares pairings of adjacent elements. According to the sorting criteria, the algorithm swaps elements to shift elements towards the beginning or end of the list.

Bubble sort is known for not being the most efficient of the sorting algorithms. If the list is completely sorted before the algorithm is called, it still has to look through each element to make sure, which is linear time.

## Merge Sort
Merge sort is a divide-and-conquer sorting algorithm that breaks the list-to-be-sorted into smaller parts. In a divide-and-conquer algorithm, the data is continually broken down into smaller elements until sorting them becomes incredibly simple.

It’s important to note that merge sort makes a copy of the entire list during its process, meaning it does not sort in place, which adds to the space complexity.

## Quicksort
Quicksort is an efficient algorithm. A single element, the pivot, is chosen from the list. All the remaining values are partitioned into two sub-lists containing the values smaller than and greater than the pivot element. When the dividing step returns sub-lists that have one or fewer elements, each sub-list is sorted. The sub-lists are recombined, or swaps are made in the original array, to produce a sorted list of values.

Ideally, this process of dividing the array will produce sub-lists of nearly equal length, otherwise, the runtime of the algorithm suffers.

## Comparisons
Take a look at the table below to see the best, average, and worst runtimes, as well as space complexities for our sorting algorithms:

|Best Case	| Worst Case | Average Case |	Space Complexity |
| -- | -- | -- | -- |
| Bubble Sort | Ω(n) | O(n^2) | O(n^2) | O(1) |
| Merge Sort | Ω(n log n) | O(n log n) |  O(n log n) | O(n) |
| Quicksort | Ω(n log n) | O(n^2) | O(n log n) | O(log n) |

These sorting algorithms can be used as-is or as a foundation for more complicated and specialized algorithms.