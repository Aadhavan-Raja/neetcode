class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
            elif i == ')' and stack[-1] == '(' and stack:
                stack.pop()
            elif i == ']' and stack[-1] == '['and stack:
                stack.pop()     
            elif i == '}' and stack[-1] == '{'and stack:
                stack.pop()
            else:
                return False
        if len(stack) > 0:
            return False
        return True
