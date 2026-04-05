class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total_sum = sum(stones)
        memo = {}
        def recurse(i, sum):
            if i == len(stones):
                return total_sum - 2 * sum
            if (i, sum) in memo:
                return memo[(i, sum)]
            result = recurse(i+1, sum)
            if sum + stones[i] <= (total_sum // 2):
                result = min(result, recurse(i+1, sum + stones[i]))
            memo[(i, sum)] = result
            return result
        return recurse(0, 0)