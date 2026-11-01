class Solution:
    def minMoves(self, nums):
        m = min(nums)
        return sum(x - m for x in nums)
        