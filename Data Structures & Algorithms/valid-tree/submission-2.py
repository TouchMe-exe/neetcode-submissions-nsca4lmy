class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        adj_list = defaultdict(list)
        visited = set()

        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        def dfs(n, par):
            
            if n in visited:
                return False

            visited.add(n)
            
            for e in adj_list[n]:
                if e == par:
                    continue
                if not dfs(e, n):
                    return False
            
            return True
        
        return dfs(0,-1) and len(visited) == n


        

        