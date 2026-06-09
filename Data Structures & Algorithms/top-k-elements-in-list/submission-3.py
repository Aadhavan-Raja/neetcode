class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in nums]
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        for i, x in freq.items():
            buckets[x-1].append(i)
        results = []
        for i in reversed(buckets):
            for j in i:
                if len(results) >= k:
                    return results
                results.append(j)
        return results
