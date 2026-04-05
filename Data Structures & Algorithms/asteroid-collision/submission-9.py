class Solution:
    def asteroidCollision(self, ast: List[int]) -> List[int]:
        stack=[]

        for a in ast:
            if stack and stack[-1]>0 and a<0:
                while stack and stack[-1]>0 and stack[-1] < -a:
                    stack.pop()
                if stack and stack[-1] == -a:
                    stack.pop()
                    continue
                if not stack or stack[-1]<0:
                    stack.append(a)
            else:
                stack.append(a)    

        return list(stack)
                    


                
        

                


            

        