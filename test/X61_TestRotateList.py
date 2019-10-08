import unittest

from X61_RotateList import Solution
from listNode import ListNode

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        head = ListNode.constructFromList([1,2,3,4,5])
        k = 2
        res = sol.rotateRight(head, k)

        self.assertTrue(res.equalToList([4,5,1,2,3]))


    def test2(self):
        sol = Solution()
        head = ListNode.constructFromList([0,1,2])
        k = 4
        res = sol.rotateRight(head, k)

        self.assertTrue(res.equalToList([2,0,1]))

    
       
if __name__ == "__main__":
    unittest.main()