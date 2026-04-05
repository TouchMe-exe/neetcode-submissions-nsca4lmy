class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        maj=nums[0]
        for i in range(len(nums)):
            if count==0:
                maj=nums[i]
            if maj==nums[i]:
                count+=1
            elif maj!=nums[i]:
                count-=1

        return maj 

