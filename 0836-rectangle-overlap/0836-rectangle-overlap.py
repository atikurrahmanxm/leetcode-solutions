
class Solution:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        return (
            rec1[0] < rec2[2] and
            rec1[2] > rec2[0] and
            rec1[1] < rec2[3] and
            rec1[3] > rec2[1]
        )
