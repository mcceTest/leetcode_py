import unittest
from X143_ReorderList import Solution
from listNode import ListNode

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        head = ListNode.constructFromList([1,2,3,4])
        sol.reorderList(head)
        self.assertTrue(head.equalToList([1,4,2,3]))

    def test2(self):
        sol = Solution()
        head = ListNode.constructFromList([1,2,3,4, 5])
        sol.reorderList(head)
        self.assertTrue(head.equalToList([1,5,2,4,3]))

    def test3(self):
        sol = Solution()
        head = ListNode.constructFromList([1])
        sol.reorderList(head)
        self.assertTrue(head.equalToList([1]))

    def test4(self):
        sol = Solution()
        head = ListNode.constructFromList([1, 2])
        sol.reorderList(head)
        self.assertTrue(head.equalToList([1, 2]))

    def test5(self):
        sol = Solution()
        head = ListNode.constructFromList([1, 2, 3])
        sol.reorderList(head)
        self.assertTrue(head.equalToList([1, 3, 2]))


if __name__ == "__main__":
    unittest.main()