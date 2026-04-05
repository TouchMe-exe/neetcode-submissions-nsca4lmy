class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        Set=set(nums)
        longest=0
        for s in Set:
            if (s-1) not in Set:
                length=1
                curr=s
                while (curr+1) in Set:
                    length+=1
                    curr+=1
                longest=max(longest,length)
        return longest        





    


                    

