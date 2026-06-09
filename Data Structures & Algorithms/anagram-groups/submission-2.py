class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            charTup = [0] * 26
            for i in word:
                charTup[ord(i) - ord('a')] += 1
            groups[tuple(charTup)] = groups.get(tuple(charTup), []).append(word)
        return list(groups.values())