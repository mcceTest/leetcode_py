'''
 Add Two Numbers
Medium

5871

1519

Favorite

Share
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from listNode import ListNode    
    

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carryOver = 0
        cur1 = l1
        cur2 = l2

        head = cur = ListNode(0)

        while cur1 != None and cur2 != None:
            curSum = cur1.val + cur2.val + carryOver
            carryOver = curSum // 10
            curVal = curSum - carryOver * 10

            newNode = ListNode(curVal)
            cur.next = newNode
            cur = newNode
            cur1 = cur1.next
            cur2 = cur2.next

        for aCur in [cur1, cur2]:
            while aCur != None:
                curSum = aCur.val + carryOver
                carryOver = curSum // 10
                curVal = curSum - carryOver * 10

                newNode = ListNode(curVal)
                cur.next = newNode
                cur = newNode
                aCur = aCur.next

        if carryOver != 0:
            cur.next = ListNode(carryOver)
            

        return head.next


    @staticmethod
    def main():
        sol = Solution()

        l1 = ListNode.constructFromList([2,4,3])
        
        l2 = ListNode.constructFromList([5,6,4])
        
        print(sol.addTwoNumbers(l1, l2).equalToList([7,0,8]))


if __name__ == "__main__":
    Solution.main()
