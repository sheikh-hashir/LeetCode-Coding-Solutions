# Intuition
The problem asks us to find how many servers received zero requests during a specific time interval `[query - x, query]` for multiple queries. A brute-force approach of checking every query against all logs would be too slow. Since the intervals change dynamically, so process the queries **offline** by sorting them. Sorting both the logs and the queries by time allows us to use a two-pointer sliding window to efficiently maintain the count of active servers within the changing window.

# Approach
1. **Sort Logs and Queries:** First sort `logs` chronologically by their timestamp (`log[1]`). Also sort the `queries` while keeping track of their original indices to populate the result array correctly.
2. **Sliding Window Configuration:** Mintain two pointers, `left` and `right`, to track the boundaries of the logs that fall into the current query window `[query - x, query]`.
3. **Expand Window (`right` pointer):** For each sorted query, advance the `right` pointer to include all logs that have a timestamp less than or equal to `query`. As new logs enter, track the server ID in a frequency map (`count`). If a server's count transitions from `0` to `1`, it becomes an active server.
4. **Shrink Window (`left` pointer):** Next, advance the `left` pointer to remove logs that have a timestamp strictly less than `query - x`. If a server's request frequency drops to `0`, it is no longer active.
5. **Record Result:** The number of servers that received at least one request is `active_servers`. Therefore, the number of servers with zero requests is simply `n - active_servers`. Store this in our result array at the query's original index.

# Complexity
- Time complexity:
\[O(M \log M + Q \log Q)\]
*Where \(M\) is the number of logs and \(Q\) is the number of queries. Sorting the logs takes \(O(M \log M)\) and sorting the queries takes \(O(Q \log Q)\). The sliding window pointers `left` and `right` traverse the logs array at most once across all queries, contributing an \(O(M)\) pass. Dictionary lookups run in \(O(1)\) on average.*

- Space complexity:
\[O(M + Q)\]
*Use \(O(Q)\) space to store the sorted queries and the final result array. The `count` hash map tracks unique active servers, which can hold up to \(O(\min(M, n))\) elements.*

# Code
```python3 []
class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        # Sort logs chronologically by timestamp
        logs.sort(key=lambda log: log[1])

        # Pair queries with their original indices and sort them
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))

        count = defaultdict(int)
        left = right = 0
        active_servers = 0

        result = [0] * len(queries)

        for query, idx in sorted_queries:
            start, end = query - x, query

            # Expand the window to include valid logs up to 'end'
            while right < len(logs) and logs[right][1] <= end:
                server = logs[right][0]

                if count[server] == 0:
                    active_servers += 1

                count[server] += 1
                right += 1

            # Shrink the window to remove stale logs before 'start'
            while left < right and logs[left][1] < start:
                server = logs[left][0]

                count[server] -= 1

                if count[server] == 0:
                    active_servers -= 1

                left += 1

            # Total servers minus active servers gives zero-request servers
            result[idx] = n - active_servers

        return result
```