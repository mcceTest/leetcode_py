'''
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

 

Example:



BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false
 

Note:

next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
You may assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when next() is called.
'''

from treeNode import TreeNode
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.st = []
        self.root = root
        ## TODO: extract this part as a method
        cur = root
        while cur is not None:
            self.st.append(cur)
            cur = cur.left
        

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        top = self.st.pop(-1)
        cur = top.right
        while cur is not None:
            self.st.append(cur)
            cur = cur.left

        return top.val

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return len(self.st) != 0
        




    @staticmethod
    def main():
        root = TreeNode.constructFromLevelList([7,3,5,None, None, 9, 20])
        it = BSTIterator(root)
        print(it.next()) 

        
if __name__ == "__main__":
    BSTIterator.main()

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()