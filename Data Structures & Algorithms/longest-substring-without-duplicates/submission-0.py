class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,0
        count=0
        maxcount=0
        charSet=set()
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
                count-=1
            charSet.add(s[r])
            count+=1
            maxcount=max(maxcount,count)
        return maxcount
            
