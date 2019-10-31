'''
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
'''


from listNode import ListNode
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None:
            return head

        dummyHead = ListNode(-1)
        dummyHead.next = head

        pre = dummyHead
        cur = head
        curLess = dummyHead

        while cur is not None:
            if cur.val < x:
                if cur == curLess.next:
                    curLess = cur
                    pre = cur
                    cur = cur.next
                else:
                    pre.next = cur.next
                    cur.next = curLess.next
                    curLess.next = cur
                    curLess = cur
                    cur = pre.next
            else:
                pre = cur
                cur = cur.next

        return dummyHead.next

            



        
    @staticmethod
    def main():
        sol = Solution()
        head = ListNode.constructFromList([1,4,3,2,5,2])
        x = 3
        print(sol.partition(head, x))

        

if __name__ == "__main__":
    Solution.main() 