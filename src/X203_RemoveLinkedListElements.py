'''
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
'''

from listNode import ListNode
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummyNode = ListNode(0)
        dummyNode.next = head
        pre = dummyNode
        cur = head
        while cur is not None:
            nxt = cur.next
            if cur.val == val:
                cur.next = None
                pre.next = nxt
            else:
                pre = cur
            cur = nxt

        return dummyNode.next


    @staticmethod
    def main():
        sol = Solution()
        head = ListNode.constructFromList([1,2,6,3,4,5,6])
        val = 6
        print(sol.removeElements(head, val))
        
        
        
if __name__ == "__main__":
    Solution.main()