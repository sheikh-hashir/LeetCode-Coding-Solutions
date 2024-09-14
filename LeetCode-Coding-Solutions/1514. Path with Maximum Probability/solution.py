import heapq
from collections import defaultdict
from typing import List


class Solution:
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start_node: int,
        end_node: int,
    ) -> float:
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
                        heapq.heappush(
                            heap, (-new_prob, neighbor)
                        )  # Push as negative for max-heap behavior

            return 0  # If end node is not reachable, return 0

        return dijkstra(start_node)
