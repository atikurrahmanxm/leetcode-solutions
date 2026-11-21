
class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)

        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        # Find the new parent using the original tree
        char_stack = [[] for _ in range(26)]
        new_parent = [-1] * n

        stack = [(0, False)]

        while stack:
            node, visited = stack.pop()
            char_index = ord(s[node]) - ord('a')

            if not visited:
                # Find the closest matching ancestor
                if char_stack[char_index]:
                    new_parent[node] = char_stack[char_index][-1]
                else:
                    new_parent[node] = parent[node]

                char_stack[char_index].append(node)

                stack.append((node, True))

                for child in reversed(children[node]):
                    stack.append((child, False))

            else:
                char_stack[char_index].pop()

        # Build the final tree
        new_children = [[] for _ in range(n)]

        for node in range(1, n):
            new_children[new_parent[node]].append(node)

        # Calculate subtree sizes
        order = []
        stack = [0]

        while stack:
            node = stack.pop()
            order.append(node)

            for child in new_children[node]:
                stack.append(child)

        answer = [1] * n

        for node in reversed(order):
            if new_parent[node] != -1:
                answer[new_parent[node]] += answer[node]

        return answer
