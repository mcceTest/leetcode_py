import unittest
from X165_CompareVersionNumbers import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        version1 = "0.1"
        version2 = "1.1"
        self.assertEqual(sol.compareVersion(version1, version2), -1)

    def test2(self):
        sol = Solution()
        version1 = "1.0.1"
        version2 = "1"
        self.assertEqual(sol.compareVersion(version1, version2), 1)

    def test3(self):
        sol = Solution()
        version1 = "7.5.2.4"
        version2 = "7.5.3"
        self.assertEqual(sol.compareVersion(version1, version2), -1)

    def test4(self):
        sol = Solution()
        version1 = "1.01"
        version2 = "1.001"
        self.assertEqual(sol.compareVersion(version1, version2), 0)

    def test5(self):
        sol = Solution()
        version1 = "1.0"
        version2 = "1.0.0"
        self.assertEqual(sol.compareVersion(version1, version2), 0)


if __name__ == "__main__":
    unittest.main()