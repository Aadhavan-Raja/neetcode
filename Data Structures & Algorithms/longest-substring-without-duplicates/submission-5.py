class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longSeq = 0
        currSeq = set()
        r = 0
        l = 0
        while l < len(s):
            if s[l] not in currSeq:
                currSeq.add(s[l])
                l += 1
                longSeq = max(longSeq, len(currSeq))
            else:
                currSeq.remove(s[r])
                r -= 1
                longSeq = max(longSeq, len(currSeq))
        return longSeq
            
            