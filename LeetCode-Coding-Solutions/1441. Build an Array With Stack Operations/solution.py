class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        result = []
        current_target_index = 0
        length = len(target)
        idx = 1

        while target[-1] >= idx:
            result.append("Push")
            if idx == target[current_target_index]:
                current_target_index += 1
            else:
                result.append("Pop")
            idx += 1
        return result
