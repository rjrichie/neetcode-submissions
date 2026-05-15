class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        tab = [[0] * (n + 1) for _ in range(m + 1)] 
        tab[m-1][n-1] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                tab[i][j] += tab[i + 1][j] + tab[i][j + 1]

        return tab[0][0]