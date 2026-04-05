class Solution:

    def compute(self,piles: List[int], num: int)->int:
        time=0
        for i in range (len(piles)):
            if piles[i]%num==0:
                time+=piles[i]//num
            else:
                time+=(piles[i]//num)+1
        return time




    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxr=max(piles)
        l,r=1,maxr
        min_r=0
        while l<=r:
            m=l+((r-l)//2)
            time=self.compute(piles,m)
            if time>h:
                l=m+1
            else:
                min_r=m
                r=m-1
        
        return min_r
            
        