'''
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
'''

from treeNode import TreeNode
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



## NOTE: convert the recursive solution to the iterative one
#      root -> left -> right
#   => root -> left -> left.left -> left.right -> right

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        st = [root]
        res = []
        while st:
            # cur is the root a sub tree
            cur = st.pop(-1)
            while cur:
                res.append(cur.val)
                if cur.right:
                    st.append(cur.right)
                cur = cur.left
                
        return res


    def preorderTraversal2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        st = []
        st.append(root)

        res = []
        while st:
            top = st.pop(-1)
            res.append(top.val)
            if top.right is not None:
                st.append(top.right)
            if top.left is not None:
                st.append(top.left)

        return res



    @staticmethod
    def main():
        sol = Solution()
        root = TreeNode.constructFromLevelList([1, None, 2, 3])
        print(sol.preorderTraversal(root))

if __name__ == "__main__":
    Solution.main() 
        