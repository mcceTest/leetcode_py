import unittest

class TestSum(unittest.TestCase):
    def test1(self):
        self.assertEqual(2, 1 * 2, "1 == 1")


if __name__ == "__main__":
    unittest.main()