import unittest
from X142_LinkedListCycleII import Solution
from listNode import ListNode

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        # head = [3,2,0,-4], pos = 1
        n1 = ListNode(3)
        n2 = ListNode(2)
        n3 = ListNode(0)
        n4 = ListNode(-4)

        n1.next = n2
        n2.next = n3
        n3.next = n4

        n4.next = n2
        
        self.assertTrue(sol.detectCycle(n1) == n2)

    def test2(self):
        sol = Solution()
        # head = [1,2], pos = 0
        n1 = ListNode(1)
        n2 = ListNode(2)
        
        n1.next = n2
        n2.next = n1
        
        self.assertTrue(sol.detectCycle(n1) == n1)

    def test3(self):
        sol = Solution()
        # head = [1], pos = -1
        n1 = ListNode(1)
        
        self.assertIsNone(sol.detectCycle(n1))

    def test4(self):
        sol = Solution()
        # head = [1, 2], pos = -1
        n1 = ListNode(1)
        n2 = ListNode(2)
        n1.next = n2
        
        self.assertIsNone(sol.detectCycle(n1))

    


if __name__ == "__main__":
    unittest.main()