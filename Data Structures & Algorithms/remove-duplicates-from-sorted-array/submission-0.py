class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums_map = {}

        for i in range(len(nums)):
            nums_map[nums[i]] = 1 + nums_map.get(nums[i], 0)
            
        i = 0
        for num in nums_map.keys():
            nums[i] = num
            i += 1

        return len(nums_map)
