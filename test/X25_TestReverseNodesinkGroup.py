import unittest

from X25_ReverseNodesinkGroup import Solution
from listNode import ListNode

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()

        head = ListNode.constructFromList([1, 2, 3, 4, 5])
        head = sol.reverseKGroup(head, 2)

        self.assertTrue(head.equalToList([2, 1, 4, 3, 5]))


    def test2(self):
        sol = Solution()

        head = ListNode.constructFromList([1, 2, 3, 4, 5])
        head = sol.reverseKGroup(head, 3)

        self.assertTrue(head.equalToList([3, 2, 1, 4, 5]))

    
    def test3(self):
        sol = Solution()

        head = ListNode.constructFromList([1, 2, 3, 4, 5])
        head = sol.reverseKGroup(head, 5)

        self.assertTrue(head.equalToList([5, 4, 3, 2, 1]))

    
    def test4(self):
        sol = Solution()

        head = ListNode.constructFromList([1, 2, 3, 4, 5])
        head = sol.reverseKGroup(head, 1)

        self.assertTrue(head.equalToList([1, 2, 3, 4, 5]))
    

    
        
       
if __name__ == "__main__":
    unittest.main()