'''
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
'''

from pprint import pprint as pp

## Idea: roate the matrix layer by layer

## TODO: try below
'''
/*
* clockwise rotate
* first reverse up to down, then swap the symmetry 
* 1 2 3     7 8 9     7 4 1
* 4 5 6  => 4 5 6  => 8 5 2
* 7 8 9     1 2 3     9 6 3
*/
'''

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        for layer in range(len(matrix) // 2):
            self.rotateLayer(matrix, layer)
        

    def rotateLayer(self, matrix, layer):
        for col in range(layer, len(matrix) - 1 - layer):
            self.rotateLayerCell(matrix, layer, col)


    def rotateLayerCell(self, matrix, layer, col):
        n = len(matrix)
        tmp = matrix[layer][col]

        matrix[layer][col] = matrix[n - 1 - col][layer]
        matrix[n - 1 - col][layer] = matrix[n - 1 - layer][n - 1 - col]
        matrix[n - 1 - layer][n - 1 - col] = matrix[col][n - 1 - layer]
        matrix[col][n - 1 - layer] = tmp

    @staticmethod
    def main():
        sol = Solution()

        matrix = [
                [1,2,3],
                [4,5,6],
                [7,8,9]
                ]
        sol.rotate(matrix)

        pp(matrix)
        

if __name__ == "__main__":
    Solution.main() 