'''
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
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
    def inorderTraversal2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        res = []
        cur = root
        st = []
        while cur is not None:
            st.append(cur)
            cur = cur.left

        while st:
            top = st[-1]
            res.append(top.val)
            st.pop()

            cur = top.right
            while cur is not None:
                st.append(cur)
                cur = cur.left

        return res

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        res = []
        cur = root
        st = []
        
        while (cur is not None) or st:
            while cur is not None:
                st.append(cur)
                cur = cur.left

            top = st[-1]
            res.append(top.val)
            st.pop()
            cur = top.right

        return res

    @staticmethod
    def main():
        sol = Solution()
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)

        print(sol.inorderTraversal(root))
        

if __name__ == "__main__":
    Solution.main() 