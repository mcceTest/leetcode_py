import unittest
from X207_CourseSchedule import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        numCourses = 2
        prerequisites = [[1,0]] 
        
        self.assertTrue(sol.canFinish(numCourses, prerequisites))

    def test2(self):
        sol = Solution()
        numCourses = 2
        prerequisites = [[1,0],[0,1]]
        
        self.assertFalse(sol.canFinish(numCourses, prerequisites))


    def test3(self):
        sol = Solution()
        numCourses = 3
        prerequisites = [[1,0],[0,1]]
        
        self.assertFalse(sol.canFinish(numCourses, prerequisites))


    def test4(self):
        sol = Solution()
        numCourses = 3
        prerequisites = [[1,0]] 
        
        self.assertTrue(sol.canFinish(numCourses, prerequisites))


    def test5(self):
        sol = Solution()
        numCourses = 4
        prerequisites = [[1,0],[2,0],[3,1],[3,2]]
        
        self.assertTrue(sol.canFinish(numCourses, prerequisites))

    
    

if __name__ == "__main__":
    unittest.main()