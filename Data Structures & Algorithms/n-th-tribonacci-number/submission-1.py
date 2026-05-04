class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1

        result = [0] * (n + 1)
        result[1] = 1
        result[2] = 1

        for i in range(len(result)):
            if i + 1 < len(result) and i + 1 != 2:
                result[i + 1] += result[i]
            if i + 2 < len(result):
                result[i + 2] += result[i]
            if i + 3 < len(result):
                result[i + 3] += result[i]
        return result[n]
                
