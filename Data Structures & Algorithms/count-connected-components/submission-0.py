class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        arr = [i for i in range(n)]

        def find(node):
            if arr[node] == node:
                return node
            arr[node] = find(arr[node])
            return arr[node]

        def union(node_a, node_b):
            parent_a = find(node_a)
            parent_b = find(node_b)
            if parent_a == parent_b:
                return
            arr[parent_a] = parent_b
        
        for node_a, node_b in edges:
            union(node_a, node_b)

        components = set()
        for node in range(n):
            components.add(find(node))

        return len(components)