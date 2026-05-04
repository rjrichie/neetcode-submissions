class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        p = 0
        for i in range(x):
            if i * i == x:
                p = i
                break
            elif i * i > x: 
                p = i - 1
                break
        return p