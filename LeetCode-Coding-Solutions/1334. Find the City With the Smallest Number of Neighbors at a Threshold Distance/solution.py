import heapq
from collections import defaultdict
from typing import List


class Solution:
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
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
