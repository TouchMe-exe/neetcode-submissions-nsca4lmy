class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        if "0000" in deadends:
            return -1

        q=deque()
        q.append("0000")
        visited=set(deadends)
        depth=-1

        def bfs(num):
            for i in range(4):
                digit=str((int(num[i])+1)%10)
                next_num=num[:i]+digit+num[i+1:]
                if next_num not in visited:
                    q.append(num[:i]+digit+num[i+1:])
                digit=str((int(num[i])-1+10)%10)
                next_num=num[:i]+digit+num[i+1:]
                if next_num not in visited:
                    q.append(num[:i]+digit+num[i+1:])


        while q:
            depth+=1
            for i in range(len(q)):
                num=q.popleft()
                if num == target:
                    return depth
                if num not in visited:
                    visited.add(num)
                    bfs(num)
        
        return -1
                    
            

            
            

        