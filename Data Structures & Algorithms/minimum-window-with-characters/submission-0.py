class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        tmap = {}
        smap = {}
        longest = 0
        longArr = [0, 0]
        for i in t:
            tmap[i] = tmap.get(i, 0) + 1
        for i in range(len(s)):
            if s[i] in tmap:
                smap[s[i]] = smap.get(s[i], 0) + 1
                l = i + 1
                while smap != tmap and l <= len(s) - 1:
                    smap[s[l]] = smap.get(s[l], 0) + 1
                if smap == tmap:
                    if l - i + 1 > longest:
                        longest = l - i + 1
                        longestArr = [i, l]
                else:
                    continue
        return s[longestArr[0], longestArr[1]]


            
            