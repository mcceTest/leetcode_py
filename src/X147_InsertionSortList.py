'''
Sort a linked list using insertion sort.


A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list
 

Algorithm of Insertion Sort:

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
'''

from listNode import ListNode
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

## TODO: create a dummy head node and rewrite it

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head

        tail = head
        cur = head.next
        while cur:
            nxt = cur.next
            if cur.val < head.val:
                tail.next = cur.next
                cur.next = head
                head = cur
            else:
                pos = head
                while pos != tail:
                    if pos.val <= cur.val and cur.val < pos.next.val:
                        tail.next = cur.next
                        cur.next = pos.next
                        pos.next = cur
                        break
                    pos = pos.next
                if pos == tail:
                    tail = cur
            cur = nxt

        return head
            
        

    @staticmethod
    def main():
        sol = Solution()
        head = ListNode.constructFromList([4,2,1,3])
        head = sol.insertionSortList(head)
        print(head)

if __name__ == "__main__":
    Solution.main()