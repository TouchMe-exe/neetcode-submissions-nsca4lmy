class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myset = set(nums)
        longest = 0

        for s in myset:
            if (s-1) not in myset:
                count = 0
                curr = s
                while curr in myset:
                    count += 1
                    curr += 1
                longest = max(longest,count)
        
        return longest





    


                    

