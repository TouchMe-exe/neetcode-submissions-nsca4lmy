class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        mem={}
        def recurse(curr_num):
            if curr_num == 0:
                return 1
            res=0
            if curr_num in mem:
                return mem[curr_num]
            for n in nums:
                if n > curr_num:
                    continue
                res+=recurse(curr_num-n)
            mem[curr_num]=res
            return res
        
        return recurse(target)