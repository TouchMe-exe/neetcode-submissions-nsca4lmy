class Solution:
    def decodeString(self, s: str) -> str:
        s_stack=[]
        c_stack=[]
        k=0
        cur=""
        for c in s:
            if c.isdigit():
                k=k*10+int(c)
            elif c=="[":
                s_stack.append(cur)
                c_stack.append(k)
                cur=""
                k=0
            elif c=="]":
                temp=cur
                cur=s_stack.pop()
                count=c_stack.pop()
                cur+=temp*count
            else:
                cur+=c
        
        return cur

        