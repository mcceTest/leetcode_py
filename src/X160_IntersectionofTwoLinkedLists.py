'''
Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:


begin to intersect at node c1.

 

Example 1:


Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
 

Example 2:


Input: intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [0,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.
 

Example 3:


Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null
Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.
 

Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
'''


from listNode import ListNode
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

## TODO: use 2 times iterations. In the first iteration, when pointer reached to the end of the current list
##       move it to the head of the other list.  In the second iteration, both pointers must meet at the
##       intersection or at the end of the list (None)

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None

        la = self.findLength(headA)
        lb = self.findLength(headB)

        hs = headA
        hl = headB
        if la > lb:
            hs = headB
            hl = headA

        cs = hs
        cl = hl
        for _ in range(abs(la - lb)):
            cl = cl.next

        while cl is not None:
            if cs == cl:
                return cs
            else:
                cs = cs.next
                cl = cl.next

        return None


    def findLength(self, head):
        cur = head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next

        return count

    @staticmethod
    def main():
        sol = Solution()
        head = ListNode.constructFromList([8,4,5])

        headA = ListNode(4)
        headA.next = ListNode(1)
        headA.next.next = head

        headB = ListNode(5)
        headB.next = ListNode(0)
        headB.next.next = ListNode(1)
        headB.next.next.next = head

        print(sol.getIntersectionNode(headA, headB))

if __name__ == "__main__":
    Solution.main()