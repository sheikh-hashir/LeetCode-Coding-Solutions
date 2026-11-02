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
