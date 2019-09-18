'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''

from listNode import ListNode
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from queue import PriorityQueue

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None

        class QItem(object):
            def __init__(self, node):
                self.key = node.val
                self.node = node

            def __lt__(self, other):
                return self.key < other.key


        pq = PriorityQueue()
        for l in lists:
            if l is not None:
                pq.put(QItem(l))

        dummy = ListNode(0)
        cur = dummy

        while not pq.empty():
            topItem = pq.get().node
            cur.next = topItem
            cur = cur.next
            if topItem.next is not None:
                pq.put(QItem(topItem.next))

        return dummy.next
        
        
    @staticmethod
    def main():
        sol = Solution()

        l1 = ListNode.constructFromList([1, 4, 5])
        
        l2 = ListNode.constructFromList([1, 3, 4])

        l3 = ListNode.constructFromList([2, 6])

        lists = [l1, l2, l3]

        head = sol.mergeKLists(lists)

        print(head)
        
if __name__ == "__main__":
    Solution.main()  