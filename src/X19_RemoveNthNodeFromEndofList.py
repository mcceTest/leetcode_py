'''
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
'''

from listNode import ListNode
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head is None:
            return None

        dummyHead = ListNode(0)
        dummyHead.next = head

        cur = dummyHead
        right = head
        for _ in range(n):
            right = right.next

        while right is not None:
            right = right.next
            cur = cur.next

        cur.next = cur.next.next
        
        return dummyHead.next


    @staticmethod
    def main():
        sol = Solution()

        head = ListNode.constructFromList([1, 2, 3, 4, 5])
        print(head)

        head = sol.removeNthFromEnd(head, 1)

        print(head)


        
if __name__ == "__main__":
    Solution.main()   