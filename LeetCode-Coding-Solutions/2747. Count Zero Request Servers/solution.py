class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda log: log[1])

        sorted_queries = sorted((q, i) for i, q in enumerate(queries))

        count = defaultdict(int)
        left = right = 0
        active_servers = 0

        result = [0] * len(queries)

        for query, idx in sorted_queries:
            start, end = query - x, query

            while right < len(logs) and logs[right][1] <= end:
                server = logs[right][0]

                if count[server] == 0:
                    active_servers += 1

                count[server] += 1
                right += 1

            while left < right and logs[left][1] < start:
                server = logs[left][0]

                count[server] -= 1

                if count[server] == 0:
                    active_servers -= 1

                left += 1

            result[idx] = n - active_servers

        return result
