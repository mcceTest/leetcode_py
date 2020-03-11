'''
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
'''

from listNode import ListNode
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head

        return self.helper(head)[0]

    
    def helper(self, head):
        if head is None or head.next is None:
            return head, head

        tail = head
        tail.next = None
        newHead, newTail = self.helper(head.next)
        if newTail is not None:
            newTail.next = tail

        return newHead, tail


    def reverseList2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head

        pre = None
        cur = head

        while cur is not None:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        return pre
    
        

    @staticmethod
    def main():
        sol = Solution()
        head = ListNode.constructFromList([1,2])
        print(sol.reverseList(head))
        
if __name__ == "__main__":
    Solution.main()