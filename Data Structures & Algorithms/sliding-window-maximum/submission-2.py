class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        import heapq
        pq = []
        for i in range(k):
            heapq.heappush(pq, -nums[i])
        for i in range(k, len(nums)):
            res.append(-pq[0])
            pq.remove(-nums[i-k])
            heapq.heapify(pq)
            heapq.heappush(pq, -nums[i])
        res.append(-pq[0])
        return res