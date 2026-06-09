class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = 0
        l, r = 0, len(heights) - 1
        while l < r:
            area = min(heights[l], heights[r]) * r - l + 1
            maxA = max(area, maxA)
            if heights[l] < heights[r]:
                if heights[l] < heights[l + 1]:
                    l += 1
                else:
                    r -= 1
            else:
                if heights[r] < heights[r - 1]:
                    r-= 1
                else:
                    l += 1
            return maxA