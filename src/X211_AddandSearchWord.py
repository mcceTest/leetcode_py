'''
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z
'''



class TrieNode(object):
    def __init__(self, val=''):
        self.val = val
        self.children = {}
        self.wordEnd = False

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        curNode = self.root
        for c in word:
            if c not in curNode.children:
                curNode.children[c] = TrieNode(c)
            curNode = curNode.children[c]
        curNode.wordEnd = True


    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.dfs(self.root, word, 0)


    def dfs(self, curNode, word, idx):
        if idx == len(word):
            return curNode.wordEnd

        c = word[idx]
        if c == '.':
            for k,v in curNode.children.items():
                if self.dfs(v, word, idx + 1):
                    return True
            return False
        else:
            if c in curNode.children:
                return self.dfs(curNode.children[c], word, idx + 1)
            else:
                return False


    @staticmethod
    def main():
        sol = WordDictionary()
        sol.addWord("bad")
        sol.addWord("dad")
        sol.addWord("mad")

        print(sol.search("pad"))
        print(sol.search("bad"))
        print(sol.search(".ad"))
        print(sol.search("b.."))


if __name__ == "__main__":
    WordDictionary.main()

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)