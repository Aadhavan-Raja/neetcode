class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        stack = []
        increasing = False
        stack.append(height[1])
        for i in range(1, len(height)):
            stack.append(height[i])
            if stack[i-1] < stack[i]:
                increasing = True
            if stack[i-1] > stack[i] and increasing:
                stack.remove(i)
                top = min(stack[1], stack[i-1])
                for i in stack:
                    add = top - i
                    if add > 0:
                        res += add
                stack.clear()
                stack.append(height[i])
                increasing = False
        return res



                





            
