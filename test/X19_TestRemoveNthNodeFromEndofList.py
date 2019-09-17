import unittest

from X19_RemoveNthNodeFromEndofList import Solution


from listNode import ListNode


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()

        head = ListNode.constructFromList([1, 2, 3, 4, 5])
        head = sol.removeNthFromEnd(head, 2)

        self.assertTrue(head.equalToList([1, 2, 3, 5]))


    def test2(self):
        sol = Solution()

        head = ListNode.constructFromList([1, 2, 3, 4, 5])
        head = sol.removeNthFromEnd(head, 1)

        self.assertTrue(head.equalToList([1, 2, 3, 4]))


    def test3(self):
        sol = Solution()

        head = ListNode.constructFromList([1])
        head = sol.removeNthFromEnd(head, 1)

        self.assertIsNone(head)
        
       
if __name__ == "__main__":
    unittest.main()