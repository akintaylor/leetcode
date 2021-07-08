class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
# [
#   [0,1,2,0],
#   [3,4,5,2],
#   [1,3,1,5]
# ]
        cols = len(matrix[0])
        rows = len(matrix)
        array = []
        
        for i, row in enumerate(matrix):
            for j, num in enumerate(row):
                if num == 0:
                    matrix[i] = [0] * cols
                    array.append(j)

        for i, row in enumerate(matrix):
            for j in array:
                matrix [i][j] = 0
                
        return matrix
    
                    