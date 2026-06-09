class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longSeq = 0
        currSeq = set()
        r = 0
        l = 0
        while l < len(s):
            if s[l] not in currSeq:
                currSeq.append(s[l])
                longSeq = max(longSeq, len(currSeq))
            else:
                CurrSeq.remove(s[r])
                longSeq = max(longSeq, len(currSeq))
        return longSeq
            
            