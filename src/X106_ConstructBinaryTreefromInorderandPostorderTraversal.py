'''
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7

'''

from treeNode import TreeNode
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0:
            return None

        inorderIdx = {}
        for i, v in enumerate(inorder):
            inorderIdx[v] = i

        return self.bt(inorder, postorder, 0, len(inorder) - 1, 0, len(postorder) - 1, inorderIdx)

    def bt(self, inorder, postorder, istart, iend, pstart, pend, inorderIdx):
        if istart > iend:
            return None

        curValue = postorder[pend]
        node = TreeNode(curValue)
        inIdx = inorderIdx[curValue]

        leftLength = inIdx - istart
        node.left = self.bt(inorder, postorder, istart, inIdx - 1, pstart, pstart + leftLength - 1, inorderIdx)
        node.right = self.bt(inorder, postorder, inIdx + 1, iend, pstart + leftLength, pend - 1, inorderIdx)
    
        return node

    @staticmethod
    def main():
        sol = Solution()
        inorder = [9,3,15,20,7]
        postorder = [9,15,7,20,3]
        node = sol.buildTree(inorder, postorder)
        print(TreeNode.toList(node))

if __name__ == "__main__":
    Solution.main() 