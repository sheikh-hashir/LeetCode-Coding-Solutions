import heapq
from collections import defaultdict
from typing import List


class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        graph = defaultdict(list)
        for o, c, w in zip(original, changed, cost):
            graph[o].append((c, w))

        def dijkstra(start: str, end: str) -> int:
            if start == end:
                return 0
            if start not in graph:
                return float("inf")

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
            return float("inf")

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

            if cost == float("inf"):
                return -1
            total_cost += cost

        return total_cost
