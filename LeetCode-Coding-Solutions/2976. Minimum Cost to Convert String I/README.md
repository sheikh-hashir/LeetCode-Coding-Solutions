# Topics

- Array
- Sorting
- Graph
- Shortest Path
- Dijkstra
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach

The problem can be seen as finding the shortest path in a weighted directed graph where:

- Nodes represent characters.
- Edges represent possible transformations between characters with associated costs.

**Graph Representation:**

- Use a dictionary to represent the graph, where each key is a character from `original` and each value is a list of tuples.
- Each tuple contains a character from `changed` and the corresponding cost.
- This graph will help in determining the possible transformations and their costs efficiently.

**Dijkstra's Algorithm for Shortest Path:**

- Dijkstra's algorithm is suitable for finding the shortest path in a weighted graph with non-negative weights.
- Use Dijkstra's algorithm to find the minimum cost to transform each character in `source` to the corresponding character in `target`.
- For each character in source that needs to be transformed, run Dijkstra's algorithm to find the shortest path from that character to the target character.

**Caching Results:**

- To avoid recomputing the shortest path for the same pair of characters multiple times, use a cache.
- Store the results of Dijkstra's algorithm for each character pair `(s_char, t_char)` in a dictionary.
- This ensures that each pair is computed only once, improving efficiency.

**Transformation Process:**

- Iterate through each character in the `source` string.
- If the character in `source` is the same as in `target`, continue to the next character.
- If they are different, use the cached result or compute the shortest path using Dijkstra's algorithm to find the minimum cost of transforming the current character.
- Sum these costs to get the total minimum transformation cost.
<!-- Describe your approach to solving the problem. -->

# Complexity

- Time complexity: `O(nlogn)`

  - Building the graph: `O(m)` where `𝑚`is the number of transformations.
  - Dijkstra's algorithm: For each character transformation, Dijkstra's algorithm runs in `O((V+E)logV)`, where `𝑉`is the number of unique characters and `𝐸`is the number of edges.
  - Total complexity: Since Dijkstra's algorithm is run for each character in the source string, the complexity is approximately
    `O(n⋅(V+E)logV)` where `𝑛` is the length of the source string.
  - The number of unique characters `𝑉` and edges `𝐸` is relatively small compared to `𝑛`, this can be simplified to `O(nlogn)`,
  <!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:
  - Graph representation: `O(V+E)`.
  - Cache and other auxiliary data structures: `O(V2)` in the worst case.
  <!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code

```
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        graph = defaultdict(list)
        for o, c, w in zip(original, changed, cost):
            graph[o].append((c, w))

        def dijkstra(start: str, end: str) -> int:
            if start == end:
                return 0
            if start not in graph:
                return float('inf')

            heap = [(0, start)]
            visited = {}
            while heap:
                current_cost, node = heapq.heappop(heap)
                if node in visited and visited[node] <= current_cost:
                    continue
                visited[node] = current_cost
                if node == end:
                    return current_cost
                for neighbor, edge_cost in graph[node]:
                    next_cost = current_cost + edge_cost
                    if neighbor not in visited or next_cost < visited[neighbor]:
                        heapq.heappush(heap, (next_cost, neighbor))
            return float('inf')

        # Cache to store the result of dijkstra for repeated queries
        cache = {}
        total_cost = 0

        for s_char, t_char in zip(source, target):
            if s_char == t_char:
                continue
            if (s_char, t_char) in cache:
                cost = cache[(s_char, t_char)]
            else:
                cost = dijkstra(s_char, t_char)
                cache[(s_char, t_char)] = cost

            if cost == float('inf'):
                return -1
            total_cost += cost

        return total_cost
```
