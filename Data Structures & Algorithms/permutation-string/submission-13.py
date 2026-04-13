class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s2) < len(s1):
            return False

        map_s1 = {}
        map_s2 = {}

        for i in range(len(s1)):
            map_s1[s1[i]] = 1 + map_s1.get(s1[i], 0)
        
        l = 0
        having = 0
        need = len(map_s1)

        for r in range(len(s2)):

            map_s2[s2[r]] = map_s2.get(s2[r],0) + 1
            if s2[r] in map_s1 and map_s1[s2[r]] == map_s2[s2[r]]:
                having += 1

            while having == need:
                if r-l+1 == len(s1):
                    return True

                if s2[l] in map_s1 and map_s1[s2[l]] == map_s2[s2[l]]:
                    having -= 1
                
                map_s2[s2[l]] -= 1
                l += 1

        return False  
                

                
        
