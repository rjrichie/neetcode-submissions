class Solution:
    def mySqrt(self, x: int) -> int:
        for i in range(x):
            if i * i == x:
                return i
            elif i * i < x:
                continue
            else: 
                return i - 1
        