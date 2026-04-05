class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adj_list = defaultdict(list)
        visited = set()

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        def dfs(node, prev):
            
            if node in visited:
                return False

            visited.add(node) 

            for neigh in adj_list[node]:
                if neigh == prev:
                    continue
                if not dfs(neigh, node):
                    return False

            return True
        

        return dfs(0, -1) and len(visited) == n


        
        
