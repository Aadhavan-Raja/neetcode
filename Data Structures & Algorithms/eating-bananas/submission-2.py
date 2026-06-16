class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 0
        r = max(piles)
        lowTime = -1
        k = -1
        while l < r:
            mid = (l + r) // 2
            time = 0
            for i in piles:
                time += Math.ceil(i/mid)
            if mid < k and time <= lowTime:
                lowTime = time
                k = mid
                r = mid -1
            else:
                l = mid + 1
        return k
            

