import unittest

from X71_SimplifyPath import Solution

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        path = '/home/'

        self.assertEqual(sol.simplifyPath(path), '/home')

    def test2(self):
        sol = Solution()
        path = '/../'

        self.assertEqual(sol.simplifyPath(path), '/')

    def test3(self):
        sol = Solution()
        path = '/home//foo/'

        self.assertEqual(sol.simplifyPath(path), '/home/foo')

    def test4(self):
        sol = Solution()
        path = '/a/./b/../../c/'

        self.assertEqual(sol.simplifyPath(path), '/c')

    def test5(self):
        sol = Solution()
        path = '/a/../../b/../c//.//'

        self.assertEqual(sol.simplifyPath(path), '/c')

    def test6(self):
        sol = Solution()
        path = '/a//b////c/d//././/..'

        self.assertEqual(sol.simplifyPath(path), '/a/b/c')

    

       
if __name__ == "__main__":
    unittest.main()