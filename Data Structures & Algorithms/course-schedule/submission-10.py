class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        q = deque()
        adj_list = defaultdict(list)
        in_deg = {}

        for u,v in prerequisites:               
            adj_list[v].append(u)
            in_deg[u] = 1 + in_deg.get(u, 0) 
        
        for v in range(numCourses):
            if in_deg.get(v, 0) == 0:
                q.append(v)
        
        visited = 0
        while q:
            node = q.popleft()
            visited += 1
            for neigh in adj_list[node]:
                in_deg[neigh] -= 1
                if in_deg[neigh] == 0:
                    q.append(neigh)

        return visited == numCourses
        
        
        

        


        


