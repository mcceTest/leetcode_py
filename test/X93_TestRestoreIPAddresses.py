import unittest
from X93_RestoreIPAddresses import Solution

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        s = "25525511135"

        self.assertListEqual(sorted(sol.restoreIpAddresses(s)), sorted(["255.255.11.135", "255.255.111.35"]))                     

    def test2(self):
        sol = Solution()
        s = "0000"

        self.assertListEqual(sorted(sol.restoreIpAddresses(s)), sorted(["0.0.0.0"]))  
        
                           
if __name__ == "__main__":
    unittest.main()