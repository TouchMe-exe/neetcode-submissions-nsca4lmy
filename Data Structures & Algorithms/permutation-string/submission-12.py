class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s2) < len(s1):
            return False

        map_s1 = {}
        map_s2 = {}

        for i in range(len(s1)):
            map_s1[s1[i]] = 1 + map_s1.get(s1[i], 0)
            map_s2[s2[i]] = 1 + map_s2.get(s2[i], 0)
        
        j = 0

        for i in range(len(s1), len(s2)):
            if map_s1 == map_s2:
                return True

            map_s2[s2[i]] = 1 + map_s2.get(s2[i], 0)
            map_s2[s2[j]] -= 1

            if map_s2[s2[j]] == 0:
                del map_s2[s2[j]]

            j += 1
        
        return map_s1 == map_s2
        
