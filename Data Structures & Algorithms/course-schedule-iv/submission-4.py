class Solution:
    def checkIfPrerequisite(self, numCourses: int, c: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        preq_list = defaultdict(list)

        for u,v in c:
            preq_list[u].append(v)
        
        def dfs(src, dst, visited):
            
            if src == dst:
                return True

            if (src in visited) or (src not in preq_list.keys()):
                return False
            
            visited.add(src)
            
            for e in preq_list[src]:
                if dfs(e, dst, visited):
                    return True
            
            return False
        
        res = []
        for u,v in queries:
            res.append(dfs(u,v,set()))
        
        return res

