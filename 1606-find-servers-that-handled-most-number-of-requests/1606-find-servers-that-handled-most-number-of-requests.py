import heapq

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        tree = [0] * (4 * k)

        def update(node, start, end, idx, val):
            if start == end:
                tree[node] = val
                return

            mid = (start + end) // 2

            if idx <= mid:
                update(node * 2, start, mid, idx, val)
            else:
                update(node * 2 + 1, mid + 1, end, idx, val)

            tree[node] = tree[node * 2] + tree[node * 2 + 1]

        def find(node, start, end, left, right):
            if end < left or start > right or tree[node] == 0:
                return -1

            if start == end:
                return start

            mid = (start + end) // 2

            result = find(node * 2, start, mid, left, right)

            if result != -1:
                return result

            return find(node * 2 + 1, mid + 1, end, left, right)

        for i in range(k):
            update(1, 0, k - 1, i, 1)

        busy = []
        handled = [0] * k

        for i in range(len(arrival)):
            time = arrival[i]

            while busy and busy[0][0] <= time:
                _, server = heapq.heappop(busy)
                update(1, 0, k - 1, server, 1)

            preferred = i % k

            server = find(1, 0, k - 1, preferred, k - 1)

            if server == -1:
                server = find(1, 0, k - 1, 0, preferred - 1)

            if server == -1:
                continue

            update(1, 0, k - 1, server, 0)

            handled[server] += 1

            heapq.heappush(
                busy,
                (time + load[i], server)
            )

        maximum = max(handled)

        return [
            i for i in range(k)
            if handled[i] == maximum
        ]