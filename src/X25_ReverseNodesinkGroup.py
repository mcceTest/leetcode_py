'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
'''

from listNode import ListNode
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


## TODO: recursive solution

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        totalLen = 0
        cur = head
        while cur is not None:
            totalLen += 1
            cur = cur.next

        nGroup = totalLen // k

        dummy = ListNode(0)
        groupStart = head
        preTail = dummy

        for _ in range(nGroup):
            gHead, gTail = self.reverseK(groupStart, k)
            preTail.next = gHead
            groupStart = gTail.next
            preTail = gTail

        preTail.next = groupStart

        return dummy.next


    def reverseK(self, head, k):
        tail = head

        pre = None
        cur = head
        next = cur.next
        
        for _ in range(k):
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
            
        tail.next = cur
        return (pre, tail)


    @staticmethod
    def main():
        sol = Solution()

        head = ListNode.constructFromList([1, 2, 3, 4, 5])
        print(head)
        head = sol.reverseKGroup(head, 2)
        print(head)
        
        
if __name__ == "__main__":
    Solution.main()   