class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            key=[0]*26
            for e in s:
                key[ord(e)-ord('a')]+=1
            res[tuple(key)].append(s)
        return list(res.values())
