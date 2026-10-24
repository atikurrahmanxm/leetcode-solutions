class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n = len(nums)
        seen = set()
        duplicate = 0

        for num in nums:
            if num in seen:
                duplicate = num
            seen.add(num)

        missing = 0

        for num in range(1, n + 1):
            if num not in seen:
                missing = num
                break

        return [duplicate, missing]
