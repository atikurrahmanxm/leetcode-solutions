class Solution:
    def minMoves(self, nums: list[int]) -> int:
        maximum = max(nums)

        moves = 0

        for num in nums:
            moves += maximum - num

        return moves