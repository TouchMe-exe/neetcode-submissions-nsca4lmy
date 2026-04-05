class Solution:
    def twoSum(self, nums: List[int], k: int) -> List[int]:
        i,j=0,len(nums)-1
        res=[]
        while i<j:
            _sum=nums[i]+nums[j]
            if _sum<k:
                i+=1
            elif _sum>k:
                j-=1
            else:
                res.append(i+1)
                res.append(j+1)
                break
        return res
                
            