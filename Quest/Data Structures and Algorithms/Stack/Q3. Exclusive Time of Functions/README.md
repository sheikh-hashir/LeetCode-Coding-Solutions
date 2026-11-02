# Approach
1. **Initialize Tracking Containers:** Create a `result` array of size `n` to store the cumulative execution times and a `stack` containing `[function_id, start_or_resume_time]` tracking points.
2. **Process Start Logs:** When a function launches:
   - If the stack is not empty, a parent function is currently active and is about to be preempted. Calculate its run duration up to this point (`time - stack[-1][1]`) and add it to its total time.
   - Then push the newly active `[funtion_id, time]` pair onto the stack.
3. **Process End Logs:** When a function stops:
   - The ending function must match the function currently at the top of the stack. Pop it and calculate its execution interval inclusively: `time - prev_start + 1`.
   - If a parent function remains on the stack below it, that parent function resumes execution at the very next timestamp (`time + 1`). Update the checkpoint timestamp of the parent on the top of the stack (`stack[-1][1] = time + 1`) to guarantee no double-counting occurs when it eventually finishes or pauses again.

# Complexity
- Time complexity:
`O(M)`
*Where \(M\) is the total number of log strings in the input list. Iterate through the log entries exactly once, executing only \(O(1)\) constant-time operations (string splitting, array index updates, stack additions, and stack deletions) per log.*

- Space complexity:
`O(M)`
*In the worst-case scenario where all function calls are unique and deeply nested inside one another, the stack will hold up to \(M / 2\) elements simultaneously, scaling linearly with the size of the log input.*

# Code
```python3 []
class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        result = [0] * n
        stack = [] # [function_id, start_or_resume_time]

        for log in logs:
            funtion_id, action, time = log.split(":")
            funtion_id = int(funtion_id)
            time = int(time)

            if action == "start":
                if stack:
                    result[stack[-1][0]] += time - stack[-1][1]
                stack.append([funtion_id, time])

            elif action == "end":
                prev_function_id, prev_start = stack.pop()
                result[prev_function_id] += time - prev_start + 1

                if stack:
                    stack[-1][1] = time + 1

        return result
```