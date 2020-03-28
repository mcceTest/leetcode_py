import unittest
from X210_CourseScheduleII import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        numCourses = 2
        prerequisites = [[1,0]] 
        
        self.assertListEqual(sol.findOrder(numCourses, prerequisites), [0, 1])

    def test2(self):
        sol = Solution()
        numCourses = 2
        prerequisites = [[1,0],[0,1]]
        
        self.assertListEqual(sol.findOrder(numCourses, prerequisites), [])


    def test3(self):
        sol = Solution()
        numCourses = 3
        prerequisites = [[1,0],[0,1]]
        
        self.assertListEqual(sol.findOrder(numCourses, prerequisites), [])


    def test4(self):
        sol = Solution()
        numCourses = 3
        prerequisites = [[1,0]] 
        
        self.assertIn(sol.findOrder(numCourses, prerequisites), [[0,1,2], [2,0,1], [0,2,1]])


    def test5(self):
        sol = Solution()
        numCourses = 4
        prerequisites = [[1,0],[2,0],[3,1],[3,2]]
        
        self.assertIn(sol.findOrder(numCourses, prerequisites), [[0,1,2,3], [0,2,1,3]])

    
    

if __name__ == "__main__":
    unittest.main()