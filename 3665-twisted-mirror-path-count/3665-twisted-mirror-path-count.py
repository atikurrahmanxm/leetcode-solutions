import sys
from functools import lru_cache

class Solution:
    def uniquePaths(self, grid):
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        dr = [0, 1]  # 0: right, 1: down
        dc = [1, 0]

        sys.setrecursionlimit(10000)

        @lru_cache(maxsize=None)
        def resolve(r, c, d):
            if r < 0 or r >= m or c < 0 or c >= n:
                return -1
            if grid[r][c] == 0:
                return r * n + c
            d2 = 1 - d
            return resolve(r + dr[d2], c + dc[d2], d2)

        def step(r, c, d):
            nr, nc = r + dr[d], c + dc[d]
            res = resolve(nr, nc, d)
            if res == -1:
                return None
            return (res // n, res % n)

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        for r in range(m):
            for c in range(n):
                if dp[r][c] == 0:
                    continue
                for d in (0, 1):
                    nxt = step(r, c, d)
                    if nxt is not None:
                        nr, nc = nxt
                        dp[nr][nc] = (dp[nr][nc] + dp[r][c]) % MOD
        return dp[m - 1][n - 1]