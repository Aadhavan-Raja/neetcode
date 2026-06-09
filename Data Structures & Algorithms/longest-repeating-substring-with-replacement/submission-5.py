class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        currWin = set()
        for r in range(len(s)):
            currWin.add(s[r])
            if len(s[l:r+1]) - len(currWin) <= k:
                res = max(res, len(s[l:r+1]))
            while len(s[l:r+1]) - len(currWin) > k:
                if s[l] in currWin:
                    currWin.remove(s[l])
                l += 1
        return res