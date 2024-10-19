

# CIA-1  
## Search Algorithms

### Introduction

Search algorithms are essential tools in computer science, used to retrieve data from various structures efficiently. This project explores 12 different search algorithms, each tailored for specific scenarios and types of data.

### Algorithms Overview

1. **British Museum Search (BMS)**
   - **Description**: BMS involves exploring all possible solutions in lexicographical order without backtracking. It explores all paths in the search space until the solution is found, allowing multiple solutions to be discovered.

2. **Depth First Search (DFS)**
   - **Description**: An uninformed search method that explores as deep as possible along a branch before backtracking to previous nodes. DFS is suitable for problems where the solution path is long but narrow.

3. **Breadth First Search (BFS)**
   - **Description**: BFS explores all nodes at the current depth level before moving on to the next. It guarantees finding the shortest path in an unweighted graph, making it a key strategy for many graph-based problems.

4. **Hill Climbing Search**
   - **Description**: A variant of DFS that incorporates heuristics to choose the next node. If there is a tie, lexicographical ordering is used. The algorithm continues moving towards a higher "elevation" or better solution until it reaches a peak.

5. **Beam Search**
   - **Description**: A constrained version of BFS, beam search limits the number of nodes considered at each level to a fixed beam width, reducing memory and processing requirements.

6. **Oracle Search**
   - **Description**: An extension of the British Museum Search that considers the work done so far and evaluates the progress towards the solution. It measures the efficiency of the search at each stage.

7. **Branch and Bound (B&B)**
   - **Description**: An informed search that utilizes an oracle to prune unnecessary paths. B&B applies cost comparisons to guide the search, allowing it to exit early when a solution is guaranteed without backtracking.

8. **Branch and Bound with Extended Lists**
   - **Description**: This algorithm implements the Dead Horse Principle (DHP), ensuring that visited nodes are not re-explored. It prioritizes nodes with lower costs than the oracle, avoiding exhaustive searches.

9. **Branch and Bound with Heuristics and Estimates**
   - **Description**: Enhances the B&B approach by incorporating heuristics to estimate the cost, leading to more informed decisions and potentially faster solutions.

10. **A* Search**
    - **Description**: A* is a combination of B&B and heuristic-based search. It uses the cost and estimates, along with an oracle and DHP, to efficiently find the optimal path with minimal resource use.

11. **AO* Search**
    - **Description**: A variant of A* used for directed acyclic graphs. It optimally solves problems that can be divided into smaller subproblems, recombining solutions for optimal results.

12. **Best First Search**
    - **Description**: An informed search method that selects the next node based on the lowest cost estimate from a heuristic function. This makes it suitable for problems where a good estimate of the cost is available.

### Implementation

Each search algorithm has been implemented in Python, with the following components:

1. **Algorithm Functions**: Individual functions implement the logic of each algorithm.
2. **Visualization**: Selected algorithms include visual representations using `matplotlib` to illustrate how they explore the search space.

### Results

Running the scripts for each algorithm will yield the following outputs:

- Search paths taken by each algorithm, visualized where applicable.

---

# CIA-2  
## Minimax and Alpha-Beta Pruning Algorithms

### Introduction

In two-player games, each player aims to maximize their own score while minimizing their opponent's. The Minimax algorithm evaluates possible future moves to identify the optimal strategy. Alpha-Beta Pruning improves this process by cutting off branches that don't need to be explored, making the algorithm more efficient.

### Algorithms Overview

1. **Minimax Algorithm**
   - **Description**: The Minimax algorithm evaluates game positions, assuming that both players play optimally. It works by minimizing the maximum loss that can occur in a given scenario.
   - **Time Complexity**: O(b^d), where b is the branching factor and d is the depth of the search tree.
   - **Space Complexity**: O(b * d).

2. **Alpha-Beta Pruning**
   - **Description**: Alpha-Beta Pruning is an optimization technique that reduces the number of nodes Minimax needs to evaluate by pruning branches that cannot influence the final decision.
   - **Time Complexity**: O(b^(d/2)) in the best case, which effectively doubles the search depth compared to plain Minimax.
   - **Space Complexity**: O(b * d).

### Implementation

The Minimax and Alpha-Beta Pruning algorithms are implemented in Python, featuring:

1. **Node Class**: Represents nodes in the game tree, including relevant game state data.
2. **Minimax Function**: Executes the Minimax algorithm for decision-making.
3. **Alpha-Beta Function**: Implements Alpha-Beta Pruning to optimize the search.
4. **Evaluation Functions**: Used to determine the value of terminal nodes in the game tree.
5. **Tree Visualization**: Provides a graphical representation of the game tree using `matplotlib`.
6. **User Input**: Enables dynamic game tree generation based on user-defined inputs.

### Results

Upon executing the script, the following outputs will be displayed:

- **Minimax Result**: The best possible move value determined by the Minimax algorithm.
- **Alpha-Beta Pruning Result**: The optimal move value determined by the Alpha-Beta Pruning algorithm with reduced node evaluations.

### License

This project is licensed under the MIT License. For more information, refer to the [LICENSE](LICENSE) file.

