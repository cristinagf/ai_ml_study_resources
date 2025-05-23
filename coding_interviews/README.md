# Coding Interview for a ML Engineer Position

## Pre-requisites
    - big O https://www.youtube.com/watch?v=4TUgqm2gJkE

### Data structures
https://www.youtube.com/watch?v=cQWr9DFE1ww
1. arrays
   read: O(1)
   insert/delete: O(n) (because stored consecutively in mem)

2. linked lists
   read: O(n) (because pointers. No indexes to locate element)
   insert/delete: O(1)!

3. hash maps
   key-value pairs
   unordered
   read/insert/delete O(1)!!

4. stacks
   lifo (visualize a stack of washed plates to use)
   push/ pop/ peek(at-top) O(1)

5. queues
   fifo
   enqueue/ dequeue/ front O(1)
   
6. trees
   nodes - edges
   binary: 2 children
   binary search tree: children on left are < than parent, and on right > than parent
    Binary search O(log n) ! (e.g., search in a lexicon/dict)

7. graphs
   nodes - edges
   no restrictions as in trees (direction, cycles)
   e.g uber userNode distanceEdge - find shortest path

8. sets
   similar to lists, but keep only unique values
   behind the scenes there are hash maps, which makes them efficient

9.  heaps
   specialized data structure modeled like a tree, but behaves as a queue
   min heap (root on min values), max heap (root on max values)
   typically don't support operations like delete but identify important items/ return/ queue next item on importance (Restructuring/ degradation in performance)
   prioritizes - It's a priority queue
   e.g., scheduling (packet handling)
   Heaps are implemented differently in languages but are essentially graphs with extra constraints. 
   Heaps sort information in order to quickly return min and max values. 
   They employ a binary approach, and depending on the implementation, a heap will have the largest or smallest value as the root. 
   Each branch of the heap will follow a sequential pattern. 
   - Complete, tree, 2 children max/ min-heap: Root is min, e/node <= than parents,
   - Fill e/level: top-bottom, left-right, except last level (can be incomplete) 

10. maps


### Algorithms

1. Search
   - baseline: linear exploration (for search)
     - go through all elements O(n) - inefficient
  
   - binary search
     - find pos of specific element in a SORTED LIST
     - e.g., guess number in a large range, is it x/2? higher? lower?
     - o(log(n))
  
   TREES AND GRAPHS:
   - depth-first search (DFS)
     - go deepest of one branch, then go to unvisited branch (backtracking)
     - array: 'visited': keeps track
     - e.g., maze solving
     - O(V + E)  vertices(nodes) + edges (branches)
  
   - breadth-first search (BFS)
     - look at nodes at one level before going deeper
     - arrays: 'visited', 'neighbors' of node
     - e.g., chess. best move at each turn. 

2. Sorting
   - insertion sort
     - traverse elements in list and compare then swap
     - best case: O(n) already sorted
     - worst case: O(n2) go through all elements
     - ok when lists are already-somewhat-sorted or small
  
   - merge sort
     - divide-and-conquer/ recursive
     - e.g., split array in pair-arrays, sort them, then merge and repeat
     - best and worst case O(n log(n))
     - not use if lists are already-somewhat-sorted or small
     - better for large and unsorted
     - Space complexity  O(n)
  
   - quick sort
     - divide-and-conquer/ recursive
       - sublist separation
         - pick a pivot number (ideally middleof list), and split list in 2 sublists, add pivot to end of list, 
         - Then compare l[0] l[-1] to pivot, and swap if first larger than second. 
         - Repeat compare/swap for the rest of the list
         - Swap left pointer with pivot (temporarily in last position)
       - This results in left lower than pivot, and right greater than pivot
       - Now repeat on both sides (sublists)
       - Finally put together as it's already sorted
     - best case O(n log(n))
     - worst case O(n^2)
     - average case: FASTER THAN MERGE SORT (if implemented correctly, reduce prob of worst case)
       - 2x to 3x faster than merge sort
     - Space complexity  O(log (n)) - better for memory
     - BUT: Works only if optimized!!!
  
3. Greedy
    - make best possible choice at e/local decision point
    - NOT for efficiency (just not best gral outcome)
      - easy to implemnt: dfs or bfs to solve it
    - USE-WHEN large amount of nodes to go through (complex problem)
      - even not 100% accurate
      - better than random decision
    - e.g., travelling salesman when n cities (>10)
      - when optimal solution calculation is not possible/ too complex
  
4. Recursion
    - Needs: base case (exit) e.g., if n==0: return 1, recursive step e.g., else: call(x-1), and a diminishing strucutre
    - Useful in hierachical problems: e.g., traverse graph
  
5. Dynamic Programming: 
    - Paradigm that breaks problem into smaller problems
    - Aims at finding the global optimal solution
    - memoization: solve subproblem and store its result for further use
    - e.g. optimal path finding
    - tabulation
  
6. Sliding windows: 2 pointers

## Key concepts
1. Binary
  - Use of 0/1
  - In appearance restrictive, binary can offer versatility of options and powerful data representations
  - e.g., ASCII binary code mapped characters map, high number of Lock combinations by a small number of binary digits
  - Boolean Logic: Map 2 inputs to a value e.g., Not (not), Or (|), And (&), Xor (^). 
   Python: a << n	Bitwise left shift, a >> n	Bitwise right shift
  - `f'{5:08b}'`  print binary representation of number five
   or get a string consisting of a binary literal -prefix 0b- with the command bin as in: `bin(5)`.
  - Convert to integer `int('0b0101', 2)`

2. Integers in python
  - char   1 byte (-128 +127)
  - short  2 bytes
  - int    4 bytes
  - long   8 bytes
  
3. Memory
  - [Stack and Heap](https://courses.grainger.illinois.edu/cs225/fa2022/resources/stack-heap/)


## Interview: Live Coding
1. Read the problem
2. Ask questions:
    - get clarificatios
    - state your assumptions e.g., data type, max, mins
    - catch edge cases!  e.g., no validation of x is required
  
3. Apply pattern recognition
    - What kind of problem is this? which data structure/ algorithm does it need?
    - Simplify the problem
    - Walk through a raw solution (speak about time/space complexity/ data, decisions, tradeoffs)
    - Work into an optimal solution
  
4. Implementation path
    - practice patterns
  
5. Debug


## Practice sources
- hackerank
- leetcode
- agents (chatGPT, deepSeek, Claude, etc)
