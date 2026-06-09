class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longSeq = 0
        currSeq = set()
        l = 0
        r = 0
        while r < len(s):
            if s[r] not in currSeq:
                currSeq.add(s[r])
                r += 1
                longSeq = max(longSeq, len(currSeq))
            else:
                currSeq.remove(s[l])
                l += 1
                longSeq = max(longSeq, len(currSeq))
        return longSeq
            
            