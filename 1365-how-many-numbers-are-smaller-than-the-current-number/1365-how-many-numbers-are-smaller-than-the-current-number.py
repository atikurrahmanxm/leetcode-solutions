class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        result = []

        for num in nums:
            count = 0

            for other in nums:
                if other < num:
                    count += 1

            result.append(count)

        return result
