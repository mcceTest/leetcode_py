'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''
from listNode import ListNode

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2

        if l2 is None:
            return l1

        dummy = ListNode(0)
        cur = dummy
        while l1 is not None and l2 is not None:
            if l2.val < l1.val:
                cur.next = l2
                l2 = l2.next
                cur = cur.next
            else:
                cur.next = l1
                l1 = l1.next
                cur = cur.next

        while l1 is not None:
            cur.next = l1
            l1 = l1.next
            cur = cur.next

        while l2 is not None:
            cur.next = l2
            l2 = l2.next
            cur = cur.next

        return dummy.next


    @staticmethod
    def main():
        sol = Solution()

        l1 = ListNode.constructFromList([1, 2, 4])
        l2 = ListNode.constructFromList([1, 3, 4])

        head = sol.mergeTwoLists(l1, l2)
        print(head)

        
        
if __name__ == "__main__":
    Solution.main()   