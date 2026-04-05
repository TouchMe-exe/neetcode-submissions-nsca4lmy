class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj_list = defaultdict(list)

        for u,v in prerequisites:               
            adj_list[v].append(u)

        for u,v in prerequisites:
            if not adj_list[u]:       
                adj_list[u]
        

        def dfs(s, visited):

            if adj_list[s] == []:
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
        


