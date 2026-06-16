class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = -1
        while l <= r:
            mid = (l + r) // 2
            time = 0
            for i in piles:
                time += math.ceil(i/mid)
            if time <= h:
                r = mid - 1
                res = mid
            else:
                l = mid + 1
        return res
            

