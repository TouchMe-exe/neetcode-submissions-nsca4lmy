class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        cur_max = 0
        l = 0
        res = 0
        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            cur_max = max(cur_max, freq[s[r]])

            while (r-l+1) - cur_max > k:
                freq[s[l]] -= 1
                l += 1

            res = max(res, r-l+1)

        return res 


            




                




                  

