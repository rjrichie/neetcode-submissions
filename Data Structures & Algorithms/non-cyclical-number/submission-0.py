class Solution:
    def isHappy(self, n: int) -> bool:
        hm = defaultdict(int)
        hm[n] = 1

        while n != 1:
            n = self.sumSquareDigits(n)
            if not hm.get(n):
                hm[n] = 1 + hm.get(n, 0)
            else:
                return False
        
        return True
    
    def sumSquareDigits(self, n: int) -> int:
        sum = 0
        x = n
        while x != 0:
            sum += (x % 10) ** 2
            x = x // 10
        return sum