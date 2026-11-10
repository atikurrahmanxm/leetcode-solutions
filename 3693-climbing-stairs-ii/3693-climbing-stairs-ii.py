class Solution:
    def climbStairs(self, n: int, costs: list[int]) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            for jump in range(1, 4):
                if i - jump >= 0:
                    cost = costs[i - 1] + jump * jump
                    dp[i] = min(dp[i], dp[i - jump] + cost)

        return dp[n]