class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap = {}
        tmap = {}
        if len(t) != len(s):
            return False
        for i in range(len(s)):
            smap[s[i]] = smap.get(s[i], 0) + 1
            tmap[t[i]] = tmap.get(t[i], 0) + 1
        return smap == tmap