class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == "(" or i == "[" or "{":
                stack.append(i)
            elif i == ')' and stack[len(stack)] == ')':
                stack.pop()
            elif i == ']' and stack[len(stack)] == ']':
                stack.pop()     
            elif i == '}' and stack[len(stack)] == '}':
                stack.pop()
            else:
                return False
        return True
