import unittest
from X92_ReverseLinkedListII import Solution
from listNode import ListNode

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        head = ListNode.constructFromList([1,2,3,4,5])
        m = 2
        n = 4
        self.assertTrue(sol.reverseBetween(head, m, n).equalToList([1,4,3,2,5]))

    def test2(self):
        sol = Solution()
        head = ListNode.constructFromList([1,2,3,4,5])
        m = 2
        n = 2
        self.assertTrue(sol.reverseBetween(head, m, n).equalToList([1,2,3,4,5]))

    def test3(self):
        sol = Solution()
        head = ListNode.constructFromList([1,2,3,4,5])
        m = 2
        n = 5
        self.assertTrue(sol.reverseBetween(head, m, n).equalToList([1,5,4,3,2])) 

    def test4(self):
        sol = Solution()
        head = ListNode.constructFromList([1,2,3,4,5])
        m = 1
        n = 4
        self.assertTrue(sol.reverseBetween(head, m, n).equalToList([4,3,2,1,5]))    

    def test5(self):
        sol = Solution()
        head = ListNode.constructFromList([1,2,3,4,5])
        m = 1
        n = 5
        self.assertTrue(sol.reverseBetween(head, m, n).equalToList([5,4,3,2,1]))                                            

if __name__ == "__main__":
    unittest.main()