'''
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.
 

Example 1:


Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Example 2:


Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
Example 3:



Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
Example 4:

Input: head = []
Output: []
Explanation: Given linked list is empty (null pointer), so return null.
 

Constraints:

-10000 <= Node.val <= 10000
Node.random is null or pointing to a node in the linked list.
Number of Nodes will not exceed 1000.
'''


"""
# Definition for a Node.
"""
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return None
        nodesMap = {}
        cur = head
        while cur is not None:
            newNode = Node(cur.val)
            nodesMap[cur] = newNode
            cur = cur.next

        cur = head
        while cur is not None:
            curMapped = nodesMap[cur]
            if cur.next is not None:
                curMapped.next = nodesMap[cur.next]
            if cur.random is not None:
                curMapped.random = nodesMap[cur.random]
            cur = cur.next

        return nodesMap[head]

    @staticmethod
    def main():
        sol = Solution()
        # head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
        n1 = Node(7)
        n2 = Node(13)
        n3 = Node(11)
        n4 = Node(10)
        n5 = Node(1)

        n1.next = n2
        n2.next = n3
        n3.next = n4
        n4.next = n5

        n2.random = n1
        n3.random = n5
        n4.random = n3
        n5.random = n1

        n = sol.copyRandomList(n1)

        print(n.val)
        print(n.next.val)
        print(n.next.random.val)


if __name__ == "__main__":
    Solution.main() 