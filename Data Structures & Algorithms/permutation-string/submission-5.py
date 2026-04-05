class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        set1={}
        l=0
        n=len(s1)

        for i in range (len(s1)):
            set1[s1[i]] = 1+set1.get(s1[i],0)

        m=len(s2)
        for i in range (len(s2)):
            set2={}
            for j in range (n):
                set2[s2[(i+j)%m]]=1+set2.get(s2[(i+j)%m],0)
            if set1==set2:
                return True
        
        return False


            