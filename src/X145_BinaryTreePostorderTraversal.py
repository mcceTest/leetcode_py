'''
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?
'''

from treeNode import TreeNode
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.postorderTraversalHelper(root, res)

        return res


    def postorderTraversalRecursive(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.postorderTraversalHelper(root, res)

        return res

    def postorderTraversalHelper(self, root, res):
        if root is not None:
            self.postorderTraversalHelper(root.right, res)
            self.postorderTraversalHelper(root.left, res)
            res.append(root.val)
        

    @staticmethod
    def main():
        sol = Solution()
        root = TreeNode.constructFromLevelList([1, None, 2, 3])
        print(sol.postorderTraversal(root))

if __name__ == "__main__":
    Solution.main() 