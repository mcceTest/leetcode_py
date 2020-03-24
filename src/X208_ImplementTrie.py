'''
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
'''

class TrieNode(object):
    def __init__(self, val='', wordEnd=False):
        self.val = val
        self.wordEnd = wordEnd
        self.children = {}

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        # self._insertChar(self.root, word, 0)

        idx = 0
        node = self.root
        while idx < len(word):
            c = word[idx]
            if c not in node.children:
                node.children[c] = TrieNode(c)
            idx += 1
            node = node.children[c]
        node.wordEnd = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        idx = 0
        node = self.root
        while idx < len(word):
            c = word[idx]
            if c not in node.children:
                return False
            else:
                idx += 1
                node = node.children[c]

        return node.wordEnd 


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        idx = 0
        node = self.root
        while idx < len(prefix):
            c = prefix[idx]
            if c not in node.children:
                return False
            else:
                idx += 1
                node = node.children[c]

        return True


    @staticmethod
    def main():
        obj = Trie()
        obj.insert("apple")
        print(obj.search('apple'))
        print(obj.search('app'))
        

if __name__ == "__main__":
    Trie.main()



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)