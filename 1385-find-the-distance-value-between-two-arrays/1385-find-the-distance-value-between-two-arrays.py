
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0

        for num in arr1:
            far = True

            for x in arr2:
                if abs(num - x) <= d:
                    far = False
                    break

            if far:
                count += 1

        return count
