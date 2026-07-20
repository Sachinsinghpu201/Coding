class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None
        """

        zeros = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):

                if matrix[i][j] == 0:
                    zeros.append([i, j])

        for row, col in zeros:

            for i in range(len(matrix[0])):
                matrix[row][i] = 0

            for j in range(len(matrix)):
                matrix[j][col] = 0

        return matrix