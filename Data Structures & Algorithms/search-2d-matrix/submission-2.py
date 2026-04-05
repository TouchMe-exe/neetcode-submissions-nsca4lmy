class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows, cols = len(matrix), len(matrix[0])
        l, r = 0 , (rows * cols) - 1

        while l<=r:
            m = l + (r-l) // 2

            i = m//cols
            j = m % cols

            if target < matrix[i][j]:
                r = m - 1
            elif target > matrix[i][j]:
                l = m + 1
            else:
                return True
        
        return False


