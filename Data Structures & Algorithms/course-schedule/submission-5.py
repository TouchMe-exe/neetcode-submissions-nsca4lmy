class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj_list = defaultdict(list)

        for u,v in prerequisites:               
            adj_list[v].append(u)
        

        def dfs(s, visited):

            if s not in adj_list:
                return True

            if s in visited:
                return False

            visited.add(s)

            for e in adj_list[s]:
                if not dfs(e, visited):
                    return False

            return True
        
        for k in adj_list.keys():
            visited = set()
            if not dfs(k, visited):
                return False

        return True
        


