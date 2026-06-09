class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tmap = {}
        minimum = float("inf")
        minArr = [0, 0]
        for ch in t:
            tmap[ch] = tmap.get(ch, 0) + 1
        for i in range(len(s)):
            if s[i] not in tmap:
                continue
            smap = {}
            for r in range(i, len(s)):
                if s[r] in tmap:
                    smap[s[r]] = smap.get(s[r], 0) + 1
                valid = True
                for ch in tmap:
                    if smap.get(ch, 0) < tmap[ch]:
                        valid = False
                        break
                if valid:
                    if r - i + 1 < minimum:
                        minimum = r - i + 1
                        minArr = [i, r]
                    break
        if minimum == float("inf"):
            return ""
        return s[minArr[0]:minArr[1] + 1]