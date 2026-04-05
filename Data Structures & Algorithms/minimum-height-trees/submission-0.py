class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        adj_list = defaultdict(list)
        h_map = [0] * n
        result = []

        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        def dfs(node, prev):
            
            height = 0
            for e in adj_list[node]:
                if e == prev:
                    continue
                height = max(height, dfs(e, node))
            
            return 1 + height
        
        
        for i in range(n):
            h_map[i] = dfs(i,-1)
        
        min_h = min(h_map)

        for i in range(n):
            if h_map[i] == min_h:
                result.append(i)
        
        return result