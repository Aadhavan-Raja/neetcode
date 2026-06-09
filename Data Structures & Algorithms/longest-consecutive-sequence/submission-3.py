class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longestSeq = 0
        for num in numSet:
            currSeq = 1
            if num - 1 in numSet:
                continue
            while num + 1 in numSet:
                currSeq += 1
                num += 1
            longestSeq = max(currSeq, longestSeq)
        return longestSeq
        
