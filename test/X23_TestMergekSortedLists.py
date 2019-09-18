import unittest

from X23_MergekSortedLists import Solution
from listNode import ListNode

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()

        l1 = ListNode.constructFromList([1, 4, 5])
        
        l2 = ListNode.constructFromList([1, 3, 4])

        l3 = ListNode.constructFromList([2, 6])

        lists = [l1, l2, l3]

        head = sol.mergeKLists(lists)

        self.assertTrue(head.equalToList([1, 1, 2, 3, 4, 4, 5, 6]))


    def test2(self):
        sol = Solution()

        l1 = ListNode.constructFromList([1, 4, 5])
        
        l2 = None

        l3 = ListNode.constructFromList([2])

        lists = [l1, l2, l3]

        head = sol.mergeKLists(lists)

        self.assertTrue(head.equalToList([1, 2, 4, 5]))


    
        
       
if __name__ == "__main__":
    unittest.main()