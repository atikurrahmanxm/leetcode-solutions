from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        total = [0] * (4 * n)
        square = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def apply(node, left, right, delta):
            length = right - left + 1
            old_sum = total[node]

            square[node] = (
                square[node] + 2 * delta * old_sum
                + delta * delta * length
            ) % MOD

            total[node] = (old_sum + delta * length) % MOD
            lazy[node] += delta

        def push(node, left, right):
            if lazy[node] and left < right:
                mid = (left + right) // 2
                apply(node * 2, left, mid, lazy[node])
                apply(node * 2 + 1, mid + 1, right, lazy[node])
                lazy[node] = 0

        def update(node, left, right, ql, qr):
            if ql <= left and right <= qr:
                apply(node, left, right, 1)
                return

            push(node, left, right)
            mid = (left + right) // 2

            if ql <= mid:
                update(node * 2, left, mid, ql, qr)

            if qr > mid:
                update(node * 2 + 1, mid + 1, right, ql, qr)

            total[node] = (
                total[node * 2] + total[node * 2 + 1]
            ) % MOD

            square[node] = (
                square[node * 2] + square[node * 2 + 1]
            ) % MOD

        last_seen = {}
        answer = 0

        for i, num in enumerate(nums):
            left = last_seen.get(num, -1) + 1

            update(1, 0, n - 1, left, i)
            last_seen[num] = i

            answer = (answer + square[1]) % MOD

        return answer