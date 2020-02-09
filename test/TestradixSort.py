from radixSort import radixSort
import unittest

class TestSum(unittest.TestCase):

    def test1(self):
        arr = [2, 10, 109,5]
        self.assertListEqual(radixSort(arr), [2,5,10,109])

if __name__ == "__main__":
    unittest.main()