# Topics
- Array
- Graph
- Heap (Priority Queue)
- Shortest Path
- Dijkstra

# Intuition
- This problem can be thought of as finding the most reliable path in a graph, where the edges are weighted by success probabilities instead of distances.
- The goal is to maximize the probability of reaching the target node from the starting node, which requires traversing the graph in a way that prioritizes higher probabilities.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach

- **Graph Representation:**
  - The first step is to represent the graph using an adjacency list. Each node in the graph has connections (edges) to other nodes, and each connection has an associated success probability.
  - We use Python's `defaultdict` from the collections module to create this adjacency list. For each edge `(node1, node2)` with a probability `succProb[idx]`, we add `(node2, succProb[idx])` to node1's list and `(node1, succProb[idx])` to node2's list.
  - This representation ensures that each node is aware of its neighboring nodes and the probability of transitioning to them.
<!-- Describe your approach to solving the problem. -->


- **Dijkstra's Algorithm:**
  - To maximize the probability of reaching the target node, we use a variation of Dijkstra's algorithm, which is typically used to find the shortest path in a graph.
  - Instead of minimizing distances, we will maximize probabilities.
  - We use a priority queue (implemented as a max-heap) to keep track of the most probable paths. Since Python's `heapq` module provides a min-heap, we simulate a max-heap by pushing negative probabilities onto the heap.
  - The algorithm begins with the start node, initializing its probability to `1` (because the probability of being at the start node is certain).
  - We then explore all neighboring nodes, updating their maximum probabilities based on the edge probabilities and the current node's probability.

- **Heap Management:**
  - We initialize the heap with the start node and its probability of 1, represented as (`-1, start_node`) to simulate a max-heap.
  - At each step, the node with the highest probability is popped from the heap, and its neighbors are examined.
  - For each neighbor, we calculate a new potential probability by multiplying the current node's probability by the edge probability.
  - If this new probability is higher than the previously recorded probability for the neighbor, we update the neighbor's probability and push it onto the heap.
  - The algorithm continues until either the target node is reached (in which case the current probability is returned) or all reachable nodes have been processed (in which case we return 0, indicating the target is unreachable).

- **Early Exit:**
  - An optimization in this approach is that we can exit early if we reach the target node while processing the heap.
  - This avoids unnecessary calculations after the goal is achieved.

- **Final Result:**
  - If the target node is reachable, the algorithm will return the highest probability found. If not, it will return 0.

# Complexity
- Time complexity: `O(ElogV)`, where `E` is the number of edges and `V` is the number of vertices (nodes).
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: `O(V+E)`, for storing the graph and additional data structures.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
import heapq
from collections import defaultdict
from typing import List

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # Step 1: Build the graph
        graph = defaultdict(list)
        for idx, (node1, node2) in enumerate(edges):
            graph[node1].append((node2, succProb[idx]))
            graph[node2].append((node1, succProb[idx]))

        # Step 2: Apply Dijkstra's Algorithm using max-heap for probabilities
        def dijkstra(source):
            heap = [(-1, source)]  # Using -1 as max probability for starting node
            max_prob = [0] * n  # Initialize probabilities for each node
            max_prob[source] = 1  # Start node has a probability of 1

            while heap:
                prob, node = heapq.heappop(heap)
                prob = -prob  # Convert back to positive probability

                if node == end_node:
                    return prob  # Early exit if end node is reached

                for neighbor, edge_prob in graph[node]:
                    new_prob = prob * edge_prob
                    if new_prob > max_prob[neighbor]:
                        max_prob[neighbor] = new_prob
                        heapq.heappush(heap, (-new_prob, neighbor))  # Push as negative for max-heap behavior

            return 0  # If end node is not reachable, return 0

        return dijkstra(start_node)

```