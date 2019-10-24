'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
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

        pre = head
        cur = head.next

        while cur is not None:
            if cur.val == pre.val:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next

        return head

    @staticmethod
    def main():
        sol = Solution()
        head = ListNode.constructFromList([1,1,2])
        print(sol.deleteDuplicates(head))

        

if __name__ == "__main__":
    Solution.main() 