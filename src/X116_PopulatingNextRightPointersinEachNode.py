'''
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

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



Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
 

Constraints:

The number of nodes in the given tree is less than 4096.
-1000 <= node.val <= 1000

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
    def connect2(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root is None:
            return root

        self.addNext(root.left, root.right)

        return root


    def addNext(self, leftRoot, rightRoot):
        if leftRoot is None:
            return

        leftRoot.next = rightRoot
        self.addNext(leftRoot.left, leftRoot.right)
        self.addNext(leftRoot.right, rightRoot.left)
        self.addNext(rightRoot.left, rightRoot.right)


    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root is None:
            return root

        start = root

        while start.left is not None:
            cur = start
            while cur is not None:
                cur.left.next = cur.right
                if cur.next is not None:
                    cur.right.next = cur.next.left
                cur = cur.next
            start = start.left

        return root
        




    @staticmethod
    def main():
        sol = Solution()
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)

        root.left.left = Node(4)
        root.left.right = Node(5)

        root.right.left = Node(6)
        root.right.right = Node(7)

        root = sol.connect(root)

        print(root.next)
        print(root.left.next.val)
        print(root.right.next)

        print(root.left.left.next.val)
        print(root.left.right.next.val)
        print(root.right.left.next.val)
        print(root.right.right.next)

if __name__ == "__main__":
    Solution.main() 
        