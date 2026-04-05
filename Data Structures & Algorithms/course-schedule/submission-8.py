class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj_list = defaultdict(list)

        for u,v in prerequisites:               
            adj_list[u].append(v)
        

        def dfs(s, visited):

            if s not in adj_list:
                return True

            if s in visited:
                return False

            visited.add(s)

            for e in adj_list[s]:
                if not dfs(e, visited):
                    return False

            adj_list.pop(s)

            return True
        
        for c in range(numCourses):
            if not dfs(c, set()):
                return False

        return True
        


