# Topics

- Graph
- Sortest Path
- Dijkstra's Algorithm
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach

To solve this problem, we can use Dijkstra's algorithm to calculate the shortest paths from each city to every other city. This will allow us to count how many cities are reachable within the given distance threshold from each city.

<!-- Describe your approach to solving the problem. -->

## Detailed Steps

1. **Graph Construction**
   We need to represent the input data (cities and roads) as a graph. Each city is a node, and each road is an edge with a weight equal to the distance between the cities. An adjacency list is suitable for this representation.
2. **Shortest Path Calculation**
   We use Dijkstra's algorithm to find the shortest path from a source city to all other cities. Dijkstra's algorithm is efficient for graphs with non-negative weights.
3. **Reachable Cities Count**
   For each city, use Dijkstra's algorithm to find the shortest paths. Count how many cities are reachable within the distance threshold.
4. Determine the Result City
   Iterate over all cities, use Dijkstra's algorithm to find the reachable cities count, and track the city with the smallest number of reachable cities. In case of a tie, prefer the city with the larger index.

# Complexity

- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code

```
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = defaultdict(list)
        for node1, node2, distance in edges:
            graph[node1].append((node2, distance))
            graph[node2].append((node1, distance))

        def dijkstra(source):
            heap = [(0, source)]
            visited = set()
            while heap:
                distance, node = heapq.heappop(heap)
                if node in visited:
                    continue
                visited.add(node)
                for neighbor, distance_2 in graph[node]:
                    neighbor_distance = distance + distance_2
                    if neighbor_distance <= distanceThreshold:
                        heapq.heappush(heap, (neighbor_distance, neighbor))

            return len(visited) - 1

        res, min_count = -1, n
        for source in range(n):
            count = dijkstra(source)
            if count <= min_count:
                res, min_count = source, count
        return res

```
