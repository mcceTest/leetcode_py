import unittest

from X49_GroupAnagrams import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        res = sol.groupAnagrams(strs)
        for l in res:
            l.sort()
        self.assertListEqual(sorted(res), sorted([
                                                    ["ate","eat","tea"],
                                                    ["nat","tan"],
                                                    ["bat"]
                                                    ]))


    
    
       
if __name__ == "__main__":
    unittest.main()