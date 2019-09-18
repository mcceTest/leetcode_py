'''
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

 

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
'''

from listNode import ListNode
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        first = head
        second = head.next
        nextStart = head.next.next
        
        head = second
        second.next = first
        first.next = self.swapPairs(nextStart)

        return head

    @staticmethod
    def main():
        sol = Solution()

        head = ListNode.constructFromList([1, 2, 3, 4])
        print(head)
        head = sol.swapPairs(head)
        print(head)
        
        
if __name__ == "__main__":
    Solution.main()   

