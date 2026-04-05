class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def pal(t):
            l = 0
            r = len(t) - 1
            while l < r:
                if t[l] != t[r]:
                    return False
                l += 1
                r -= 1
            return True

        memo = {}

        def sol(i):
            if i in memo:
                return memo[i]
            if i == len(s):
                return 0
            sol_1 = sol(i+1)
            sol_2 = 0
            for j in range(i, len(s)):
                res = pal(s[i:j+1])
                print(i, j, s[i:j+1], res)
                if res:
                    sol_2 += 1
            memo[i] = sol_1 + sol_2
            return memo[i]


        return sol(0)


            