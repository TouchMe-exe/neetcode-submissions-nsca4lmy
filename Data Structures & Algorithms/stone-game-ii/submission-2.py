class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        

        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        mem = {}

        def dp(i: int, M: int) -> int:
            
            if i >= n:
                return 0

            if (i,M) in mem:
                return mem[(i,M)]

            if 2 * M >= n - i:
                return suffix[i]

            best = 0
            
            for X in range(1, 2 * M + 1):
                
                opponent_best = dp(i + X, max(M, X))
                current_gain = suffix[i] - opponent_best
                best = max(best, current_gain)

            mem[(i,M)] = best
            return best

        return dp(0, 1)
