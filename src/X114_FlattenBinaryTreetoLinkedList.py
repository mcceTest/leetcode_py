'''
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
'''

from treeNode import TreeNode
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.flattenHelper(root)

        return root
        

    def flattenHelper(self, root):
        if root is None:
            return (None, None)

        cur = root

        lstart, lend = self.flattenHelper(root.left)
        rstart, rend = self.flattenHelper(root.right)

        if lstart is not None:
            cur.right = lstart
            cur = lend

        root.left = None

        if rstart is not None:
            cur.right = rstart
            cur = rend

        return (root, cur)

        

    @staticmethod
    def main():
        sol = Solution()
        root = TreeNode.constructFromLevelList([1, 2, 5, 3, 4, None, 6])
        root = sol.flatten(root)

        print(TreeNode.toList(root))

if __name__ == "__main__":
    Solution.main() 