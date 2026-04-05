class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s2) < len(s1):
            return False

        def check_permutation(s1, s2):
            map_s1 = {}
            map_s2 = {}

            for i in range(len(s1)):
                map_s1[s1[i]] = 1 + map_s1.get(s1[i], 0)
                map_s2[s2[i]] = 1 + map_s2.get(s2[i], 0)
            
            return map_s1 == map_s2
        
        len_s1 = len(s1)
        len_s2 = len(s2)

        i = 0
        for j in range(len_s1, len_s2 + 1):
            if check_permutation(s1, s2[i:j]):
                return True
            i += 1
        
        return False
