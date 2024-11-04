class Solution:
    def compressedString(self, word: str) -> str:
        if not word:
            return ""

        result = []
        previous_char = word[0]
        count = 1

        for index in range(1, len(word)):
            if word[index] != previous_char:
                result.append(f"{count}{previous_char}")
                previous_char = word[index]
                count = 1
            else:
                count += 1
                if count > 9:
                    result.append(f"{count - 1}{previous_char}")
                    count = 1

        result.append(f"{count}{previous_char}")

        return "".join(result)
