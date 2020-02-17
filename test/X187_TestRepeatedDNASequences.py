import unittest
from X187_RepeatedDNASequences import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
        self.assertListEqual(sorted(sol.findRepeatedDnaSequences(s)), sorted(['AAAAACCCCC', 'CCCCCAAAAA']))


if __name__ == "__main__":
    unittest.main()