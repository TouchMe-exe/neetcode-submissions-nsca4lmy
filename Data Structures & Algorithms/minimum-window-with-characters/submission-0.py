class Solution:
    def minWindow(self, s: str, t: str) -> str:
        map1={}
        map2={}
        for i in range (len(t)):
            map1[t[i]] = 0
            map2[t[i]] = 1+map2.get(t[i],0)

        l=r=0
        have,need=0,len(map2)
        resLen,res=float("infinity"),[-1,-1]
        while r < len(s):
            c=s[r]
            map1[c]=1+map1.get(c,0)

            if c in map2.keys() and map1[c]==map2[c]:
                have+=1
            
            while have==need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                if s[l] in map2.keys():
                    map1[s[l]]=map1.get(s[l],0)-1
                    if map1.get(s[l])<map2.get(s[l]):
                        have-=1
                l+=1
            r+=1
        l,r=res
        return s[l : r + 1] if resLen != float("infinity") else ""
                    
        

            





