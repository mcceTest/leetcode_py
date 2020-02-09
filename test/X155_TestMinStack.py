import unittest
from X155_MinStack import MinStack


class TestSum(unittest.TestCase):

    def test1(self):
        sol = MinStack()
        sol.push(-2)
        sol.push(-3)
        sol.push(0)
        self.assertEqual(sol.getMin(), -3)

        sol.pop()
        self.assertEqual(sol.top(), -3)
        self.assertEqual(sol.getMin(), -3)

        sol.pop()
        self.assertEqual(sol.getMin(), -2)

if __name__ == "__main__":
    unittest.main()