class Solution:
    def numSquares(self, n: int) -> int:
        arr = [n] * (n + 1)

        arr[0] = 0

        for target in range(1, n+1):
            for s in range(1, target+1):
                square = s * s
                if target - square < 0:
                    break
                arr[target] = min(arr[target], 1 + arr[target - square])
        return arr[n]