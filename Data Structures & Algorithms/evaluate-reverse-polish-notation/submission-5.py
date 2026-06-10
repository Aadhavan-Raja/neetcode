class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = float('inf')
        for i in tokens:
            if i.isdecimal():
                stack.append(i)
            elif i == '+':
                if res == float('inf'):
                    res = stack.pop() + stack.pop()
                else:
                    res += int(stack.pop())
            elif i == '*':
                if res == float('inf'):
                    res = stack.pop()*stack.pop()
                else:
                    res *= int(stack.pop())
            elif i == '-':
                if res == float('inf'):
                    res = stack.pop() - stack.pop()
                else:
                    int(res)
                    res -= int(stack.pop())
            elif i == '/':
                if res == float('inf'):
                    res = stack.pop()/stack.pop()
                else:
                    res /= int(stack.pop())  
        return res
