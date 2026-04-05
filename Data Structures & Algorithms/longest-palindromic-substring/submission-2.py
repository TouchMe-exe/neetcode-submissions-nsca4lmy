class Solution:
    def longestPalindrome(self, s: str) -> str:

        longest = 0
        
        for i in range(len(s)):
            l = i
            r = i

            while l>-1 and r<len(s) and s[l] == s[r]:
                r += 1
                l -= 1

            if longest < r-l-1:
                final_l = l+1
                final_r = r-1
                longest = r-l-1

        
        for i in range(len(s)-1):
            l = i
            r = i+1

            while l>-1 and r<len(s) and s[l] == s[r]:
                r += 1
                l -= 1

            if longest < r-l-1:
                final_l = l+1
                final_r = r-1
                longest = r-l-1
        
        return s[final_l : final_r+1]
