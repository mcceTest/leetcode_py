'''
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
'''

from listNode import ListNode
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return head

        # find the node before the mid node
        preHead2 = self.findMidNode(head)
        # print("preHead2:", preHead2)
        # reverse the nodes starting from the mid node, and return the new head
        head2 = self.reverseNodes(preHead2.next)
        # print("head2:", head2)
        preHead2.next = None

        # merge the first and second half of the list
        self.reorderTwoList(head, head2)


    def findMidNode(self, head):
        slow = head
        fast = head.next.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

    def reverseNodes(self, head):
        pre = None
        cur = head

        while cur is not None:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        return pre

    def reorderTwoList(self, head1, head2):
        cur1 = head1
        cur2 = head2

        while True:
            nxt1 = cur1.next
            nxt2 = cur2.next

            cur1.next = cur2
            if nxt1 is None:
                break
            cur2.next = nxt1

            cur1 = nxt1
            cur2 = nxt2
        

    @staticmethod
    def main():
        sol = Solution()
        head = ListNode.constructFromList([1,2,3,4,5])
        print(head)

        sol.reorderList(head)
        print(head)


if __name__ == "__main__":
    Solution.main() 