class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def bsearch(l: int,r: int,target: int,nums: List[int])->int:
            while l<=r:
                m=l+((r-l)//2)
                if (nums[m]<target):
                    l=m+1
                elif(nums[m]>target):
                    r=m-1
                else:
                    return m
            return -1
        
        def find_pivot(l: int,r: int,nums: List[int])->int:
            while l<r:
                m=l+(r-l)//2

                if(nums[m]>nums[r]):
                    l=m+1
                else:
                    r=m
            return l

        l,r=0,len(nums)-1
        pivot=find_pivot(l,r,nums)
        print(pivot)
        res=bsearch(l,pivot-1,target,nums)
        if res == -1:
            res=bsearch(pivot,r,target,nums)
        
        return res



