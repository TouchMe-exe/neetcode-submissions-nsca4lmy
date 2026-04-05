class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        preq_list = defaultdict(list)
        q = deque()
        res = []
        in_deg = {}
        finish = 0

        for u,v in prerequisites:
            preq_list[v].append(u)
            in_deg[u] = 1 + in_deg.get(u, 0)

        for i in range(numCourses):
            if in_deg.get(i, 0) == 0:
                q.append(i)

        while q:
            node = q.popleft()
            res.append(node)
            finish += 1

            for e in preq_list[node]:
                in_deg[e] -= 1
                if in_deg[e] == 0:
                    q.append(e)
            
        if finish == numCourses:
            return res
        else:
            return []
            




        
        

        
        

            


        

