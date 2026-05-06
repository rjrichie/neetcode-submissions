class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Find potential row
        i, j = 0, len(matrix) - 1
        while i <= j:
            mid = int((i + j) / 2)
            row_min = matrix[mid][0]
            row_max = matrix[mid][-1]
            if target >= row_min and target <= row_max:
                # Check potential row
                n, m = 0, len(matrix[mid]) - 1
                while n < m:
                    mid2 = int((n + m) / 2)
                    el = matrix[mid][mid2]
                    if target == el:
                        return True
                    elif target < el:
                        m = mid2 - 1
                    else:
                        n = mid2 + 1
                return False
            elif target < row_min:
                # Check previous rows
                j = mid - 1
            elif target > row_max:
                # Check next rows
                i = mid + 1
        return False
            
