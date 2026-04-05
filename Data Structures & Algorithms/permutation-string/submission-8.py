class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1)>len(s2):
            return False
            
        map1 = {}
        map2 = {}

        for i in range(len(s1)):
            map1[s1[i]] = 1 + map1.get(s1[i], 0)
            map2[s2[i]] = 1 + map2.get(s2[i], 0)

        l = 0
        r = len(s1)

        while r < len(s2):
            if map1 == map2:
                return True
            
            map2[s2[r]] = 1 + map2.get(s2[r], 0)
            map2[s2[l]] = map2.get(s2[l], 0) - 1

            if map2[s2[l]] == 0:
                del map2[s2[l]]

            r += 1
            l += 1
        
        return map1 == map2




            