class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])

        result = []

        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)

        return result
