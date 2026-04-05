class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        l,r=max(weights),sum(weights)
        min_s=r
        i=0
        while l<=r:

            m=l+((r-l)//2)
            day=0
            i=0
            while i<len(weights):    
                capacity=0
                print("min_s",m)
                while i<len(weights) and capacity<=m:
                    capacity+=weights[i]
                    i+=1
                day+=1
                if(i < len(weights)):
                    i-=1
                else:
                    if(capacity>m):
                        day+=1



    
            if day<=days:
                min_s=min(min_s,m)
                r=m-1
            else:
                l=m+1

        return min_s




        