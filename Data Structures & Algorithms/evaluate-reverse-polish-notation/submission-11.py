class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in "+*-/":
                stack.append(int(i))
            else:
                if i == '+':
                    var2 = stack.pop()
                    var1 = stack.pop()
                    stack.append(var1+var2)
                elif i == '-':
                    var2 = stack.pop()
                    var1 = stack.pop()
                    stack.append(var1-var2)
                elif i == '*':
                    var2 = stack.pop()
                    var1 = stack.pop()
                    stack.append(var1*var2)
                elif i == '/':
                    var2 = stack.pop()
                    var1 = stack.pop()
                    stack.append(Math.floor(var1/var2))
        return stack[0]

