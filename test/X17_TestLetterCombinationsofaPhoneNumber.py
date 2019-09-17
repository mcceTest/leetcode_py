import unittest
from X17_LetterCombinationsofaPhoneNumber import Solution

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()

        self.assertListEqual(sorted(sol.letterCombinations("23")), sorted(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]))
        
       
if __name__ == "__main__":
    unittest.main()