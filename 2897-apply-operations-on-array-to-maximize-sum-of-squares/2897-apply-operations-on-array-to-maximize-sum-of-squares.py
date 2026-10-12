class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        MOD = 10**9 + 7
        bits = [0] * 31

        # Count occurrences of each set bit.
        for num in nums:
            for b in range(31):
                if num & (1 << b):
                    bits[b] += 1

        ans = 0

        # Construct k numbers with the largest possible values.
        for _ in range(k):
            x = 0
            for b in range(31):
                if bits[b] > 0:
                    x |= 1 << b
                    bits[b] -= 1

            ans = (ans + x * x) % MOD

        return ans