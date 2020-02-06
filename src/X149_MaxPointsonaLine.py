'''
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Example 1:

Input: [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o  
+------------->
0  1  2  3  4
Example 2:

Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
'''


class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) <= 2:
            return len(points)

        res = 0
        for i in range(len(points)):
            cur = self.maxPointsWithIdx(points, i)
            if cur > res:
                res = cur

        return res

    def maxPointsWithIdx(self, points, idx):
        slopMap = {}
        curPoint = points[idx]
        maxGroup = 0
        # only consider the points after this one
        #   as the points before it have already been considered as starting point
        for i in range(idx + 1, len(points)):
            dx = points[i][0] - curPoint[0]
            dy = points[i][1] - curPoint[1]

            slop = self.getSlop(dx, dy)
            if slop in slopMap:
                slopMap[slop] += 1
            else:
                slopMap[slop] = 1
            if slop != (0, 0):
                if slopMap[slop] > maxGroup:
                    maxGroup = slopMap[slop]
        
        return 1 + slopMap.get((0, 0), 0) + maxGroup
        
            

    def getSlop(self, dx, dy):
        if dx == 0:
            if dy == 0:
                return (0, 0)
            else:
                return (0, 1)
        
        if dy == 0:
            return (1, 0)

        if dx < 0:
            dx = -1 * dx
            dy = -1 * dy

        g = self.computeGCD(dx, dy)

        return (dx / g, dy / g)


    def computeGCD(self, x, y): 
        while y: 
            x, y = y, x % y 
        
        return x 


    @staticmethod
    def main():
        sol = Solution()
        points = [[1,1],[2,2],[3,3]]
        print(sol.maxPoints(points))

if __name__ == "__main__":
    Solution.main()