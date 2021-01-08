import kmp
import unittest

class TestSum(unittest.TestCase):

    def test1(self):
        s = "ABCABD"
        self.assertListEqual(kmp.KMPSearch(s, "A"), [0, 3])


    def test2(self):
        s = "ABCABD"
        self.assertListEqual(kmp.KMPSearch(s, "BD"), [4])


if __name__ == "__main__":
    unittest.main()
