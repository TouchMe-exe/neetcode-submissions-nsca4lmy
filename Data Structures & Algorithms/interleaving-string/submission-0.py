class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        memo = {}
        def recurse(l1, l2):
            if l1 == len(s1) and l2 == len(s2):
                return True
            elif l1 == len(s1):
                return s2[l2:] == s3[l1+l2:]
            elif l2 == len(s2):
                return s1[l1:] == s3[l1 + l2:]
            if (l1, l2) in memo:
                return memo[(l1, l2)]
            l3 = l1 + l2
            for i1 in range(l1, len(s1)):
                for i2 in range(l2, len(s2)):
                    sub1 = s1[l1:i1+1]
                    sub2 = s2[l2:i2+1]
                    len1 = len(sub1)
                    len2 = len(sub2)
                    if (
                        (sub1 + sub2 == s3[l3:l3 + len1 + len2]) 
                        and recurse(i1+1, i2+1)
                    ):
                        memo[(l1, l2)] = True
                        return True
                    if (
                        (sub2 + sub1 == s3[l3:l3 + len1 + len2])
                        and recurse(i1+1, i2+1)
                    ):
                        memo[(l1, l2)] = True
                        return True
            memo[(l1, l2)] = False
            return False
        return recurse(0, 0)
