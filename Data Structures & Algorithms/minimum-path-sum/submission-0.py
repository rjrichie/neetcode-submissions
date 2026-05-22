class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n_rows, n_cols = len(grid), len(grid[0])

        dp = [float("inf")] * (n_cols + 1)
        dp[n_cols - 1] = 0 # Start from bottom

        for row in range(n_rows-1, -1, -1):
            for col in range(n_cols-1, -1, -1):
                dp[col] = grid[row][col] + min(dp[col], dp[col + 1])
        
        return dp[0]