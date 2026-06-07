class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r = 0,len(matrix)-1

        while l <= r:
            m = (l+r)//2

            if matrix[m][0] == target:
                return True
            elif matrix[m][0] > target:
                r = m-1
            else:
                l = m+1
        
        x = r
        l,r = 0, len(matrix[0])-1
        while l <= r:
            m = (l+r) // 2

            if matrix[x][m] == target:
                return True
            elif matrix[x][m] > target:
                r = m-1
            else:
                l = m+1
        return False
        
