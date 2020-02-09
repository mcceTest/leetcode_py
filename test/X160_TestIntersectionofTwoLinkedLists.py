import unittest
from X160_IntersectionofTwoLinkedLists import Solution
from listNode import ListNode

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        head = ListNode.constructFromList([8,4,5])

        headA = ListNode(4)
        headA.next = ListNode(1)
        headA.next.next = head

        headB = ListNode(5)
        headB.next = ListNode(0)
        headB.next.next = ListNode(1)
        headB.next.next.next = head

        self.assertTrue(sol.getIntersectionNode(headA, headB).equalToList([8,4,5]))


    def test2(self):
        sol = Solution()
        head = ListNode.constructFromList([2,4])

        headA = ListNode.constructFromList([0,9,1])
        headA.next.next.next = head

        headB = ListNode(3)
        headB.next = head

        self.assertTrue(sol.getIntersectionNode(headA, headB).equalToList([2,4]))

if __name__ == "__main__":
    unittest.main()