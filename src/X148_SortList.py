'''
Sort a linked list in O(n log n) time using constant space complexity.

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

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        # 1. split the list into two
        firstHead, secondHead = self.splitList(head)

        # 2. sort the 2 sub lists
        firstHead = self.sortList(firstHead)
        secondHead = self.sortList(secondHead)

        # 3. merge the 2 sorted lists
        return self.mergeList(firstHead, secondHead)

    def splitList(self, head):
        slow = head
        fast = head.next

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        secondHead = slow.next
        slow.next = None

        return (head, secondHead)

    def mergeList(self, firstHead, secondHead):
        dummy = ListNode(0)
        firstCur = firstHead
        secondCur = secondHead
        cur = dummy

        while firstCur is not None and secondCur is not None:
            if secondCur.val < firstCur.val:
                cur.next = secondCur
                secondCur = secondCur.next
            else:
                cur.next = firstCur
                firstCur = firstCur.next
            cur = cur.next
        
        for partCur in (firstCur, secondCur):
            while partCur is not None:
                cur.next = partCur
                partCur = partCur.next
                cur = cur.next

        return dummy.next
        

    @staticmethod
    def main():
        sol = Solution()
        head = ListNode.constructFromList([4,2,1,3])
        head = sol.sortList(head)
        print(head)

if __name__ == "__main__":
    Solution.main()