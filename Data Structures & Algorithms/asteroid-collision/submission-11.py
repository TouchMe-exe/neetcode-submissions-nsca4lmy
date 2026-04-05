class Solution:
    def asteroidCollision(self, ast: List[int]) -> List[int]:
        stack=[]

        for a in ast:
            
            while stack and stack[-1]>0 and a<0:
                if abs(a) > stack[-1]:
                    stack.pop()
                else: 
                    break

            if stack and a<0:
                if stack[-1] == abs(a):
                    stack.pop()
                    continue
                elif stack[-1] > abs(a):
                    continue

            stack.append(a)

        
        return stack
                    


                
        

                


            

        