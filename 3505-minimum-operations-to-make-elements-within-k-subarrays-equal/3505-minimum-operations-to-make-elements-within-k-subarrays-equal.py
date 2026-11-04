class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        n = len(nums)

        values = sorted(set(nums))
        m = len(values)
        pos = {v: i + 1 for i, v in enumerate(values)}

        count = [0] * (m + 1)
        total = [0] * (m + 1)

        def update(bit, i, val):
            while i <= m:
                bit[i] += val
                i += i & -i

        def query(bit, i):
            s = 0
            while i:
                s += bit[i]
                i -= i & -i
            return s

        def get_median():
            target = (x + 1) // 2
            idx = 0
            step = 1 << (m.bit_length() - 1)

            while step:
                nxt = idx + step
                if nxt <= m and count[nxt] < target:
                    idx = nxt
                    target -= count[nxt]
                step >>= 1

            return idx + 1

        def add(num, delta):
            i = pos[num]
            update(count, i, delta)
            update(total, i, num * delta)

        def cost():
            mid = get_median()
            median = values[mid - 1]

            left_count = query(count, mid)
            left_sum = query(total, mid)
            all_sum = query(total, m)

            return (
                median * left_count - left_sum
                + all_sum - left_sum
                - median * (x - left_count)
            )

        costs = []
        for num in nums[:x]:
            add(num, 1)

        for i in range(n - x + 1):
            costs.append(cost())

            if i + x < n:
                add(nums[i], -1)
                add(nums[i + x], 1)

        dp = [0] * (n + 1)

        for j in range(1, k + 1):
            new_dp = [float('inf')] * (n + 1)

            for i in range(1, n + 1):
                new_dp[i] = new_dp[i - 1]

                if i >= x:
                    new_dp[i] = min(
                        new_dp[i],
                        dp[i - x] + costs[i - x]
                    )

            dp = new_dp

        return dp[n]