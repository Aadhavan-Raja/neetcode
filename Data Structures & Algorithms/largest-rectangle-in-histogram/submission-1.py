class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        leftMax = [-1] * len(heights)
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                leftMax[i] = stack[-1]
            stack.append(i)
        stack = []
        rightMax = [-1] * len(heights)
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                rightMax[i] = stack[-1]
            stack.append(i)
        maxA = 0
        for i in range(len(heights)):
            leftMax[i] += 1
            rightMax[i] -= 1
            maxA = max(maxA, heights[i] * (rightMax[i] - leftMax[i] + 1))
        return maxA