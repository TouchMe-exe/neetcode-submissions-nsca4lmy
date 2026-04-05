class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        root = [i for i in range(n)] 
        rank = [1] * n

        def find(n):
            if root[n] != n:
                root[n] = find(root[n])
            return root[n]
        
        def union(node_a, node_b):
            parent_a = find(node_a)
            parent_b = find(node_b)

            if parent_a == parent_b:
                return False
                
            if rank[parent_a] > rank[parent_b]:
                root[parent_b] = find(parent_a)
                rank[parent_b] += 1
            else:
                root[parent_a] = find(parent_b)
                rank[parent_a] += 1

            return True
        
        for u,v in edges:
            if not union(u,v):
                return False
        
        for i in range(n-1):
            if find(i) != find(i+1):
                return False

        return True    
            
            
        
