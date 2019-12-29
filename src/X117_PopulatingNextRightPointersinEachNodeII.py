'''
Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 

Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
 

Example 1:



Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
 

Constraints:

The number of nodes in the given tree is less than 6000.
-100 <= node.val <= 100
'''


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next



class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root is None:
            return root

        start = root
        while start is not None:
            cur = start
            nextStart = None
            curChild = None

            while cur is not None:
                for node in (cur.left, cur.right):                        
                    if node is not None:
                        if nextStart is None:
                            nextStart = node

                        if curChild is not None:
                            curChild.next = node
                        curChild = node
                cur = cur.next

            start = nextStart

        return root


    @staticmethod
    def main():
        sol = Solution()
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)

        root.left.left = Node(4)
        root.left.right = Node(5)

        # root.right.left = Node(6)
        root.right.right = Node(7)

        root = sol.connect(root)

        print(root.next)
        print(root.left.next.val)
        print(root.right.next)

        print(root.left.left.next.val)
        print(root.left.right.next.val)
        # print(root.right.left.next.val)
        print(root.right.right.next)

if __name__ == "__main__":
    Solution.main() 

                