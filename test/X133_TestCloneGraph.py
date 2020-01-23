import unittest
from X133_CloneGraph import Solution
from X133_CloneGraph import Node

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        # adjList = [[2,4],[1,3],[2,4],[1,3]]
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(4)

        n1.neighbors = [n2, n4]
        n2.neighbors = [n1, n3]
        n3.neighbors = [n2, n4]
        n4.neighbors = [n1, n3]

        c1 = sol.cloneGraph(n1)

        self.assertEqual(c1.val, n1.val)
        
        self.assertEqual(len(c1.neighbors), 2)

if __name__ == "__main__":
    unittest.main()