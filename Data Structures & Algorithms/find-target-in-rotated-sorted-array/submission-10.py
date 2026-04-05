class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        def bsearch(l: int,r: int,target: int)->int:
            while l<=r:
                m=l+((r-l)//2)
                if(nums[m]==target):
                    return m
                elif (nums[m]<target):
                    l=m+1
                else:
                    r=m-1
            return -1
        
        def find_pivot(l: int,r: int)->int:
            while l<r:
                m = l + (r-l) // 2

                if nums[m]<nums[r]:
                    r = m
                else:
                    l = m+1

            return l

        l, r = 0, len(nums)-1
        pivot = find_pivot(l,r)
        
        res = bsearch(l,pivot-1,target)
        if res == -1:
            res = bsearch(pivot,r,target)
        
        return res