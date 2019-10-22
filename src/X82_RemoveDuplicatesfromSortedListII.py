'''
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3
'''
from listNode import ListNode
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        newHead = ListNode(0)
        newHead.next = head
        pre = newHead
        cur = head
        

        while cur is not None:
            removeCur = False
            nxt = cur.next
            while nxt is not None and nxt.val == cur.val:
                removeCur = True
                nxt = nxt.next

            if removeCur:
                cur = nxt
                pre.next = cur
            else:
                pre = cur
                cur = nxt

        return newHead.next

            


    @staticmethod
    def main():
        sol = Solution()
        head = ListNode.constructFromList([1,2,3,3,4,4,5])
        print(sol.deleteDuplicates(head))

        

if __name__ == "__main__":
    Solution.main() 
        