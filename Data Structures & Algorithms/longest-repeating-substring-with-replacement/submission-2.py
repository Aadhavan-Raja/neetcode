class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 1
        currWin = set()
        for r in range(len(s)):
            currWin.add(s[r])
            if len(s[l:r]) - len(currWin) <= 3:
                res = max(res, len(s[l:r]))
            while len(s[l:r]) - len(currWin) > 3:
                if s[l] in currWin:
                    currWin.remove(s[l])
                l += 1
        return res