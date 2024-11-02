class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(" ")
        words.append(words[0])
        length = len(words)
        return all(words[i][0] == words[i - 1][-1] for i in range(1, length))
