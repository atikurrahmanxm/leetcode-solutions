
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        squares = sorted(x * x for x in nums)
        mid = len(nums) // 2

        return sum(squares[mid:]) - sum(squares[:mid])