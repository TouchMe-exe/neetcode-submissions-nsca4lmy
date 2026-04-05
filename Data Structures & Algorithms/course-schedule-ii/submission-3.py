class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        preq_list = defaultdict(list)
        q = deque()
        visited = []
        in_deg = numCourses * [0]
        finish = 0

        for u,v in prerequisites:
            preq_list[u].append(v)
            in_deg[v] += 1

        for i in range(numCourses):
            if in_deg[i] == 0:
                q.append(i)

        while q:
            node = q.popleft()
            visited.append(node)
            finish += 1

            for e in preq_list[node]:
                in_deg[e] -= 1
                if in_deg[e] == 0:
                    q.append(e)
            
        if finish == numCourses:
            return visited[::-1]
        else:
            return []
            




        
        

        
        

            


        

