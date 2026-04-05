class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        vocabulary = set(wordDict)
        n = len(s)
        memo = {}
        def recurse(l):
            if l >= n:
                return True
            if l in memo:
                return memo[l]
            result = False
            for i in range(l, n):
                word = s[l:i+1]
                if word in vocabulary:
                    if recurse(i+1):
                        result = True
                        break
            memo[l] = result
            return result

        return recurse(0)