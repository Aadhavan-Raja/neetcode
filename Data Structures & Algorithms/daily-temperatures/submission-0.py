class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = []
        for i in range(len(temperatures)):
            while i < len(temperatures):
                if stack[0] > temperatures[i]:
                    stack.append(temperatures[i])
                else:
                    res.append(len(stack))
                    stack.pop(0)
        return res

                

