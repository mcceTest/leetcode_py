import unittest
from X208_ImplementTrie import Trie


class TestSum(unittest.TestCase):

    def test1(self):
        obj = Trie()
        obj.insert("apple")
        self.assertTrue(obj.search('apple'))
        self.assertFalse(obj.search('app'))

        self.assertTrue(obj.startsWith('app'))

        obj.insert('app')
        self.assertTrue(obj.search('app'))
    

if __name__ == "__main__":
    unittest.main()