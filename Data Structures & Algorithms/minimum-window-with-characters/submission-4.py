class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""

        map1 = {}
        map2 = {}
        matches = 0

        for i in range (len(t)):
            map2[t[i]] = 1 + map2.get(t[i], 0)

        l = 0
        min_w = float('inf')
        min_w_str = ""

        for r in range(len(s)):

            map1[s[r]] = 1 + map1.get(s[r], 0)
            if s[r] in map2 and map1[s[r]] == map2[s[r]]:
                matches += 1

            while matches == len(map2):
                min_w_str = s[l:r+1] if r-l+1<min_w else min_w_str
                min_w = min(min_w, r-l+1)
                map1[s[l]] -= 1
                if s[l] in map2 and map1[s[l]] < map2[s[l]]:
                    matches -= 1
                l += 1
        

        return min_w_str    
        

            





