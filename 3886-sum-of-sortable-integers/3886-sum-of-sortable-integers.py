import math

class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        divisors = []
        

        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)
        
        ans = 0
        

        for k in divisors:
            valid = True
            prev_max = float('-inf')
            
            for start in range(0, n, k):
                end = start + k
                
                drops = 0
                for i in range(start, end - 1):
                    if nums[i] > nums[i + 1]:
                        drops += 1
                

                if drops > 1:
                    valid = False
                    break
                if drops == 1 and nums[start] < nums[end - 1]:
                    valid = False
                    break
                
                curr_min = min(nums[start:end])
                curr_max = max(nums[start:end])
                
                if curr_min < prev_max:
                    valid = False
                    break
                
                prev_max = curr_max
            
            if valid:
                ans += k
        
        return ans