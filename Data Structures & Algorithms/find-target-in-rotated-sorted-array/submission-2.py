class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def bsearch(l: int,r: int,target: int)->int:
            while l<=r:
                m=l+((r-l)//2)
                if (nums[m]<target):
                    l=m+1
                elif(nums[m]>target):
                    r=m-1
                else:
                    return m
            return -1
        
        def find_pivot(l: int,r: int)->int:
            while l<r:
                m = l + (r-l) // 2

                if nums[m]<nums[r]:
                    r = m-1
                else:
                    l = m+1

            return l

        l, r = 0, len(nums)-1
        pivot = find_pivot(l,r)
        print(pivot)
        res = bsearch(l,pivot,target)
        if res == -1:
            res = bsearch(pivot,r,target)
        
        return res



