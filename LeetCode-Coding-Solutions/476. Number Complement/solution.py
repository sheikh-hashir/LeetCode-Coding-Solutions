class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num)[2:]
        complement = binary.translate(str.maketrans("01", "10"))
        return int(complement, 2)
