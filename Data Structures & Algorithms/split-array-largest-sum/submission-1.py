class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def cansplit(mid: int)->bool:
            l=0
            r=len(nums)
            sum_val,split=0,1
            while l<r:
                sum_val+=nums[l]
                if sum_val>mid:
                    sum_val=0
                    split+=1
                    l-=1
                l+=1

            if split>k:
                return False
            else:
                return True
                

        l=max(nums)
        r=sum(nums)

        while l<r:
            mid=l+(r-l)//2

            if cansplit(mid):
                r=mid
            else:
                l=mid+1
            
        return l
        