class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tmap = {}
        smap = {}
        minimum = 9999
        minArr = [0, 0]
        for i in t:
            tmap[i] = tmap.get(i, 0) + 1
        for i in range(len(s)):
            if s[i] in tmap:
                smap[s[i]] = smap.get(s[i], 0) + 1
                r = i + 1
                while smap != tmap and r <= len(s) - 1:
                    if s[r] in tmap:
                        smap[s[r]] = smap.get(s[r], 0) + 1
                    r += 1
                if smap == tmap:
                    if r - i< minimum:
                        minimum = r - i
                        minArr = [i, r]
                    smap.clear()
                else:
                    smap.clear()
        return s[minArr[0]:minArr[1]+1]


            
            