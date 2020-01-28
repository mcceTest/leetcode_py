'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.

 

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:

Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:

Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.


 

Follow-up:
Can you solve it without using extra space?
'''

from listNode import ListNode
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return None

        #       -  -  - -
        #      /         \  
        # 0 - 1 - 2 - 3 - 4
        # length of the list l = 5
        # index of the node connected from tail x = 1
        # initially slow pointer index s = 0, and after the cycle start node (x=1), s(t) = x + (t - x) % c
        #    where c is the length of the cycle (if any), and c = l - x
        #  similarly after the cycle start node, the fast pointer index f(t) = x + (2 * t - x) % c
        # when the slow and fast pointers meet (at or after the cycle start node):
        #           s(t) = f(t)
        #       which x + (t - x) % c = x + (2 * t - x) % c
        #          so t % c = 0    =>  t = k * c  (here k > 0 and c > 0) 
        # Then we move the fast pointer to the head and move it one step at time,
        #     after x steps the fast pointer is at the cycle start node,
        #        and the slow point is at s(t+x) = x + (t+x - x) % c = x + (t % c) = x (as t % c = 0)
        #     the slow and fast pointers meet again the first time at the cycle start node.
        # Hence we get the cycle start node.
        slow = head.next
        fast = head.next.next

        while fast is not None and fast.next is not None:
            if slow == fast:
                fast = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
            
            slow = slow.next
            fast = fast.next.next

        return None
        

    @staticmethod
    def main():
        sol = Solution()
        # head = [3,2,0,-4], pos = 1
        n1 = ListNode(3)
        n2 = ListNode(2)
        n3 = ListNode(0)
        n4 = ListNode(-4)

        n1.next = n2
        n2.next = n3
        n3.next = n4

        n4.next = n1
        
        assert(sol.detectCycle(n1) != None)
        assert(sol.detectCycle(n1).val == 3)


if __name__ == "__main__":
    Solution.main() 