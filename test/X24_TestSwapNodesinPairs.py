import unittest

from X24_SwapNodesinPairs import Solution
from listNode import ListNode

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()

        head = ListNode.constructFromList([1, 2, 3, 4])
        head = sol.swapPairs(head)

        self.assertTrue(head.equalToList([2, 1, 4, 3]))


    def test2(self):
        sol = Solution()

        head = ListNode.constructFromList([1, 2, 3])
        head = sol.swapPairs(head)

        self.assertTrue(head.equalToList([2, 1, 3]))


    
        
       
if __name__ == "__main__":
    unittest.main()