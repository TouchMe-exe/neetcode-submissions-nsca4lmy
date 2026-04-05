class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        mem={}

        def rec(i, prev_idx):

            if i == n:
                return 0
            if (i, prev_idx) in mem:
                return mem[(i, prev_idx)]
            best = rec(i + 1, prev_idx)

            if prev_idx == -1 or nums[i] > nums[prev_idx]:
                best = max(best, 1 + rec(i + 1, i))

            mem[(i, prev_idx)] = best
            return best

        return rec(0, -1)