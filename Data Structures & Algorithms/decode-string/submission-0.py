class Solution:
    def decodeString(self, s: str) -> str:
        stringStack = []
        countStack = []
        current = ""
        k = 0

        for c in s:
            if c.isdigit():
                k = k * 10 + int(c)
            elif c == "[":
                stringStack.append(current)
                countStack.append(k)
                current, k = "", 0
            elif c == "]":
                temp = current
                current = stringStack.pop()
                count = countStack.pop()
                current += temp * count
            else:
                current += c
        return current
