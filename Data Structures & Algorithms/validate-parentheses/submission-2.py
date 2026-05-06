class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(':
                stack.append('(')
            elif c == '{':
                stack.append('{')
            elif c == '[':
                stack.append('[')
            elif c == ')':
                if stack[-1] != '(':
                    return False
                stack.pop()
            elif c == '}':
                if stack[-1] != '{':
                    return False
                stack.pop()
            elif c == ']':
                if stack[-1] != '[':
                    return False
                stack.pop()
        if len(stack) == 0:
            return True
        return False