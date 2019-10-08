'''
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
'''
from listNode import ListNode

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        listLength = 0
        cur = head
        tail = head
        while cur is not None:
            listLength += 1
            tail = cur
            cur = cur.next

        if listLength <= 1 or k % listLength == 0:
            return head

        k = k % listLength

        pre = head
        for _ in range(listLength - k - 1):
            pre = pre.next

        newHead = pre.next
        pre.next = None
        tail.next = head

        return newHead


        



    @staticmethod
    def main():
        sol = Solution()
        head = ListNode.constructFromList([1,2,3,4,5])
        k = 2
        print(sol.rotateRight(head, k))

if __name__ == "__main__":
    Solution.main() 