class Solution:
    def countSubstrings(self, s: str) -> int:
        odd_palindromes = 0
        for i in range(len(s)):
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                odd_palindromes += 1
                l -= 1
                r += 1
        even_palindromes = 0
        for i in range(len(s)-1):
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                even_palindromes += 1
                l -= 1
                r += 1
        return odd_palindromes + even_palindromes        