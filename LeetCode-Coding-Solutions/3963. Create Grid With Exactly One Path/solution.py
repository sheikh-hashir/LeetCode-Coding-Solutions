class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        result = [["#"] * n for _ in range(m)]

        row, colume = 0, 0
        count = 0

        while row < m and colume < n:
            result[row][colume] = "."

            if row == m - 1:
                colume += 1
            elif colume == n - 1:
                row += 1
            elif count % 2 == 0:
                colume += 1
            else:
                row += 1

            count += 1

        return ["".join(r) for r in result]
