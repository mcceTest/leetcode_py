import unittest

from X38_CountandSay import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()

        self.assertEqual(sol.countAndSay(5), '111221')
        
    def test2(self):
        sol = Solution()
        self.assertEqual(sol.countAndSay(1), '1')

    def test3(self):
        sol = Solution()
        self.assertEqual(sol.countAndSay(2), '11')

    def test4(self):
        sol = Solution()
        self.assertEqual(sol.countAndSay(3), '21')


    def test5(self):
        sol = Solution()
        self.assertEqual(sol.countAndSay(4), '1211')
        
       
if __name__ == "__main__":
    unittest.main()