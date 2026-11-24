
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0

        for i in range(n):
            product = 1
            g = 0
            l = 1

            for j in range(i, n):
                num = nums[j]

                product *= num
                g = gcd(g, num)
                l = l * num // gcd(l, num)

                if product == g * l:
                    result = max(result, j - i + 1)

        return result
