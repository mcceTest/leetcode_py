import unittest
from listNode import ListNode
from X86_PartitionList import Solution

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        head = ListNode.constructFromList([1,4,3,2,5,2])
        x = 3
        self.assertTrue(sol.partition(head, x).equalToList([1,2,2,4,3,5]))

    def test2(self):
        sol = Solution()
        head = ListNode.constructFromList([1,2,3])
        x = 3
        self.assertTrue(sol.partition(head, x).equalToList([1,2,3]))

    def test3(self):
        sol = Solution()
        head = ListNode.constructFromList([3,2,3])
        x = 3
        self.assertTrue(sol.partition(head, x).equalToList([2,3,3]))

    def test4(self):
        sol = Solution()
        head = ListNode.constructFromList([3,2,3])
        x = 1
        self.assertTrue(sol.partition(head, x).equalToList([3,2,3]))


if __name__ == "__main__":
    unittest.main()