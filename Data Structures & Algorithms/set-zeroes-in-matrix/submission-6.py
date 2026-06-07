class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])

        row0 = 1
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r == 0:
                        row0 = 0
                    else:
                        matrix[r][0] = 0
        
        for c in range(1,COLS):
            if matrix[0][c] == 0:
                for r in range(1, ROWS):
                    matrix[r][c] = 0
        for r in range(1,ROWS):
            if matrix[r][0] == 0:
                for c in range(1, COLS):
                    matrix[r][c] = 0
        if matrix[0][0] == 0:
            for r in range(1, ROWS):
                matrix[r][0] = 0
        if row0 == 0:
            for c in range(COLS):
                matrix[0][c] = 0
        
        
        