class Solution:

    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(s: str):
            l=0
            r=len(s)-1
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True

        output: list = []
        result: list = []

        def build_partitions(t: str):

            if len(t) == 0:
                output.append(result[:])
            
            for i in range(len(t)):
                sub1=t[:i+1]
                sub2=t[i+1:]
                print(sub1,sub2)
                if not is_palindrome(sub1):
                    continue
                
                result.append(sub1)
                build_partitions(sub2)
                result.pop()

        build_partitions(s)  
            
        return output