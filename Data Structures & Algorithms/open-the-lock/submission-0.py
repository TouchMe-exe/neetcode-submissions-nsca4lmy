class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        if "0000" in deadends:
            return -1

        q=deque()
        q.append(("0000",0))
        visited=set(deadends)


        def bfs(num):
            res=[]
            for i in range(4):
                digit=num[i]
                new_num=num[:i]+str((int(digit)+1)%10)+num[i+1:]
                res.append(new_num)
                new_num=num[:i]+str((int(digit)-1+10)%10)+num[i+1:]
                res.append(new_num)
                
            return res

        while q:
            num,step=q.popleft()
            if num == target:
                return step
            for child in bfs(num):
                if child not in visited:
                    visited.add(child)
                    q.append((child,step+1))
        
        return -1
                    
            

            
            

        