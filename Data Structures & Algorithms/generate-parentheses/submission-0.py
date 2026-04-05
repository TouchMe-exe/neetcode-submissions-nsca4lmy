class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack=[]
        res=[]

        def backtrack(openN: int, closeN: int):
            if (openN == closeN == n):
                res.append("".join(stack))
                return
            
            if (openN < n):
                stack.append("(")
                backtrack(openN+1,closeN)
                stack.pop()
            
            if (openN > closeN):
                stack.append(")")
                backtrack(openN,closeN+1)
                stack.pop()
            
        backtrack(0,0)
        return res

        