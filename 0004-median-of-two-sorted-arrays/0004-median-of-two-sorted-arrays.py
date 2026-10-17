
from typing import List

class Solution:
    def findMedianSortedArrays(
        self, nums1: List[int], nums2: List[int]
    ) -> float:

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left, right = 0, m

        while left <= right:
            i = (left + right) // 2
            j = (m + n + 1) // 2 - i

            a = float('-inf') if i == 0 else nums1[i - 1]
            b = float('inf') if i == m else nums1[i]

            c = float('-inf') if j == 0 else nums2[j - 1]
            d = float('inf') if j == n else nums2[j]

            if a <= d and c <= b:
                if (m + n) % 2 == 1:
                    return float(max(a, c))

                return (max(a, c) + min(b, d)) / 2

            elif a > d:
                right = i - 1
            else:
                left = i + 1