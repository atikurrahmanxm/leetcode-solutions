class Solution:
    def minOperations(self, nums):
        n = len(nums)
        if n == 1:
            return 0

        is_sorted_rot = True
        for i in range(1, n):
            if nums[i] != (nums[i-1] + 1) % n:
                is_sorted_rot = False
                break
        
        is_rev_rot = True
        for i in range(1, n):
            if nums[i] != (nums[i-1] - 1) % n:
                is_rev_rot = False
                break
        
        if not is_sorted_rot and not is_rev_rot:
            return -1

        if is_sorted_rot:
            k = (n - nums.index(0)) % n
            start_state = (0, k)
        else:
            k = (n - 1 - nums.index(0)) % n
            start_state = (1, k)

        from collections import deque
        queue = deque([(start_state, 0)])
        visited = {start_state}
        
        while queue:
            (is_rev, idx), dist = queue.popleft()
            if is_rev == 0 and idx == 0:
                return dist
            
            next_state_L = (is_rev, (idx + 1) % n)
            if next_state_L not in visited:
                visited.add(next_state_L)
                queue.append((next_state_L, dist + 1))
            
            next_state_R = (1 - is_rev, (n - idx) % n)
            if next_state_R not in visited:
                visited.add(next_state_R)
                queue.append((next_state_R, dist + 1))
        
        return -1