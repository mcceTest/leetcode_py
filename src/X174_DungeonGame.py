'''
The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

 

Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

-2 (K)	-3	3
-5	-10	1
10	30	-5 (P)
 

Note:

The knight's health has no upper bound.
Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.
'''



class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        nrow = len(dungeon)
        if nrow == 0:
            return 0

        ncol = len(dungeon[0])
        if ncol == 0:
            return 0

        curRow = [1] * ncol
        if dungeon[-1][-1] < 0:
            curRow[-1] = dungeon[-1][-1] * -1 + 1

        for col in range(ncol - 2, -1, -1):
            target = curRow[col + 1] - dungeon[-1][col]
            if target > 1:
                curRow[col] = target

        for row in range(nrow - 2, -1, -1):
            preRow = curRow[:]
            curRow = [1] * ncol
            for col in range(ncol - 1, -1, -1):
                if col == ncol - 1:
                    target = preRow[col] - dungeon[row][col]
                else:
                    target = min(curRow[col + 1], preRow[col]) - dungeon[row][col]
                if target > 1:
                    curRow[col] = target

        return curRow[0]
        

    @staticmethod
    def main():
        sol = Solution()
        dungeon = [
            [0, -3]
        ]
        print(sol.calculateMinimumHP(dungeon))
        
if __name__ == "__main__":
    Solution.main()