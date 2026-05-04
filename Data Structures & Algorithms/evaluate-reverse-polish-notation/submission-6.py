class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for token in tokens:
            if token == "+":
                a = stack.pop()
                b = stack.pop()
                res = a + b
                stack.append(res)
            elif token == "*":
                a = stack.pop()
                b = stack.pop()
                res = a * b
                stack.append(res)
            elif token == "-":
                a = stack.pop()
                b = stack.pop()
                res = b - a
                stack.append(res)
            elif token == "/":
                a = stack.pop()
                b = stack.pop()
                res = int(b / a)
                stack.append(res)
            else:
                stack.append(int(token))
        return stack[-1]