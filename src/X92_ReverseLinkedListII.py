'''
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
'''
from listNode import ListNode

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head is None or m == n:
            return head

        dummyHead = ListNode(-1)
        dummyHead.next = head

        pre = dummyHead
        cur = head
        nxt = head.next

        preStart = tail = None

        for _ in range(m - 1):
            pre = cur
            cur = nxt
            nxt = cur.next

        preStart = pre
        tail = cur

        for _ in range(n - m + 1):
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
            

        preStart.next = pre
        tail.next = cur

        return dummyHead.next


    @staticmethod
    def main():
        sol = Solution()
        head = ListNode.constructFromList([1,2,3,4,5])
        m = 2
        n = 4
        print(sol.reverseBetween(head, m, n))
        

if __name__ == "__main__":
    Solution.main() 
