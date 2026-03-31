class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.prefixMat = [[0] * (COLS + 1) for r in range(ROWS + 1)]
        for r in range(ROWS):
            prefix = 0 
            for c in range(COLS):
                prefix += matrix[r][c]
                above = self.prefixMat[r][c+1]
                self.prefixMat[r + 1][c + 1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        bottomRight = self.prefixMat[row2][col2]
        above = self.prefixMat[row1-1][col2]
        left = self.prefixMat[row2][col1-1]
        topleft = self.prefixMat[row1 -1][col1 - 1]
    
        return bottomRight - above - left + topleft

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)