class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mem={}
        def recurse(step):
            if step>=len(cost):
                return 0
            if step in mem:
                return mem[step]
            mem[step]=cost[step]+min(recurse(step+1),recurse(step+2))
            return mem[step]
        return min(recurse(0),recurse(1))
                
            
