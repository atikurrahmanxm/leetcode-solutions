class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        row = [0] * m
        col = [0] * n

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row[i] += 1
                    col[j] += 1

        result = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if row[i] > 1 or col[j] > 1:
                        result += 1

        return result