class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longestSeq = -1
        for num in nums:
            currSeq = 0
            if num - 1 in nums:
                continue
            while num + 1 in nums:
                currSeq += 1
                num += 1
            longestSeq = max(currSeq, longestSeq)
        return longestSeq
        
