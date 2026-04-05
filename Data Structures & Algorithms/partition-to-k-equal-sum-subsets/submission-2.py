from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k

        nums.sort(reverse=True)
        if nums and nums[0] > target:
            return False

        sides = [0] * k

        def dfs(index: int) -> bool:
            if index == len(nums):
                return True
            v = nums[index]
            for i in range(k):
                if sides[i] + v <= target:
                    sides[i] += v
                    if dfs(index + 1):
                        return True
                    sides[i] -= v

                if sides[i] == 0:
                    break
            return False

        return dfs(0)
