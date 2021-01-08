from countSort import countSort
import unittest

class TestSum(unittest.TestCase):

    def test1(self):
        arr = [2,1,3, 1]
        self.assertListEqual(countSort(arr), [1,1,2,3]) 
        
    def test2(self):
        arr = [2,1,3, 1, 1]
        self.assertListEqual(countSort(arr, lambda x: x % 2), [2,1,3, 1, 1]) 

    def test3(self):
        arr = [2,1,3, 1, 1, 4]
        self.assertListEqual(countSort(arr, lambda x: x % 2), [2,4, 1,3, 1, 1]) 


if __name__ == "__main__":
    unittest.main()