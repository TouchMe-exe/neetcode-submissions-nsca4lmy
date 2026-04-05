class Solution:
    def checkIfPrerequisite(self, numCourses: int, c: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        preq_list = defaultdict(list)
        preq_map = [set() for _ in range(numCourses)]
        visited = set()

        for u,v in c:
            preq_list[v].append(u)
        
        def dfs(src, u, visited):
            
            if src not in preq_list.keys():
                preq_map[u].add(src)
                return

            if src in visited:
                return
            
            visited.add(src)
            preq_map[u].add(src)

            for e in preq_list[src]:
                dfs(e, u, visited)
    
            return
        
        for u,v in c:
            dfs(u,u,set())
            dfs(v,v,set())

    
        res = []
        #print(preq_map)
        for u,v in queries:
            res.append(u in preq_map[v])
        
        return res

