class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        arr = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(node):
            if arr[node] != node:
                arr[node] = find(arr[node])
            return arr[node]
        
        def union(node_a, node_b):
            parent_a = find(node_a)
            parent_b = find(node_b)

            if parent_a == parent_b:
                return False

            if rank[parent_a] > rank[parent_b]:
                arr[parent_b] = parent_a
                rank[parent_a] += rank[parent_b]
            else:
                arr[parent_b] = parent_a
                rank[parent_b] += rank[parent_a]
            
            return True
        
        for node_1, node_2 in edges:
            if not union(node_1, node_2):
                return [node_1, node_2]

        

        


