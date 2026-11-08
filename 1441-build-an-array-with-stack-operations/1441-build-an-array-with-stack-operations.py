class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        result = []
        index = 0

        for num in range(1, n + 1):
            result.append("Push")

            if num == target[index]:
                index += 1
            else:
                result.append("Pop")

            if index == len(target):
                break

        return result