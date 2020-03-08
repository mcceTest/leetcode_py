'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
'''


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid is None:
            return 0
        nrow = len(grid)
        if nrow == 0:
            return 0
        ncol = len(grid[0])
        if ncol == 0:
            return 0

        res = 0
        for row in range(nrow):
            for col in range(ncol):
                res += self.dfs(grid, row, col, nrow, ncol)

        return res

    
    def dfs(self, grid, row, col, nrow, ncol):
        if grid[row][col] == '0':
            return 0

        grid[row][col] = '0'
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            x = row + dx
            y = col + dy
            if x >= 0 and x < nrow and y >= 0 and y < ncol:
                self.dfs(grid, x, y, nrow, ncol)

        return 1
        

    def numIslands2(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid is None:
            return 0
        nrow = len(grid)
        if nrow == 0:
            return 0
        ncol = len(grid[0])
        if ncol == 0:
            return 0

        visited = [ [False] * ncol for _ in range(nrow)]
        res = 0
        for row in range(nrow):
            for col in range(ncol):
                res += self.dfs2(grid, row, col, nrow, ncol, visited)

        return res

    
    def dfs2(self, grid, row, col, nrow, ncol, visited):
        if visited[row][col] or grid[row][col] == '0':
            return 0

        visited[row][col] = True
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            x = row + dx
            y = col + dy
            if x >= 0 and x < nrow and y >= 0 and y < ncol:
                self.dfs2(grid, x, y, nrow, ncol, visited)

        return 1
        


    @staticmethod
    def main():
        sol = Solution()
        
        grid = [list('11110'),
                list('11010'),
                list('11000'),
                list('00000')]

        print(sol.numIslands(grid))
        
        
if __name__ == "__main__":
    Solution.main()
        