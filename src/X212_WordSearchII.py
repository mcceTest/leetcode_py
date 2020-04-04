'''
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example:

Input: 
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]
 

Note:

All inputs are consist of lowercase letters a-z.
The values of words are distinct.
'''

## Copied from X208
class TrieNode(object):
    def __init__(self, val='', wordEnd=False):
        self.val = val
        self.wordEnd = wordEnd
        self.children = {}
        self.found = False
        self.word = None

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
        node.word = word

    
## TODO: dfs search the board using the trie
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if len(board) == 0 or len(board[0]) == 0:
            return []

        ## O(n ^ 2)
        charIndices = {}
        for x in range(len(board)):
            for y in range(len(board[0])):
                c = board[x][y]
                if c not in charIndices:
                    charIndices[c] = []
                charIndices[c].append((x, y))

        trie = Trie()
        ## O(m * l)
        for word in words:
            trie.insert(word)

        visited = [ [False] * len(board[0]) for _ in range(len(board))]
        cur = []
        res = []
        self.dfs(board, charIndices, trie.root, None, None, visited, cur, res)

        return res


    def dfs(self, board, charIndices, node, x, y, visited, cur, res):
        if node.wordEnd and not node.found:
            # res.append(''.join(cur))
            node.found = True
            res.append(node.word)

        ## at most 26 character
        for c, n in node.children.items():
            if x is None:
                if c in charIndices:
                    for newX, newY in charIndices[c]:
                        visited[newX][newY] = True
                        # cur.append(c)
                        self.dfs(board, charIndices, n, newX, newY, visited, cur, res)
                        visited[newX][newY] = False
                        # cur.pop()
            else:
                for dx, dy in [(-1,0), (1, 0), (0, -1), (0, 1)]:
                    newX = x + dx
                    newY = y + dy
                    if newX >= 0 and newX < len(board) and newY >= 0 and newY < len(board[0]):
                        if board[newX][newY] == c and not visited[newX][newY]:
                            visited[newX][newY] = True
                            # cur.append(c)
                            self.dfs(board, charIndices, n, newX, newY, visited, cur, res)
                            visited[newX][newY] = False
                            # cur.pop()

    @staticmethod
    def main():
        sol = Solution()
        board = [
            ['o','a','a','n'],
            ['e','t','a','e'],
            ['i','h','k','r'],
            ['i','f','l','v']
        ]
        words = ["oath","pea","eat","rain"]
        print(sol.findWords(board, words))


class Solution3(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if len(board) == 0 or len(board[0]) == 0:
            return []

        ## O(n ^ 2)
        charIndices = {}
        for x in range(len(board)):
            for y in range(len(board[0])):
                c = board[x][y]
                if c not in charIndices:
                    charIndices[c] = []
                charIndices[c].append((x, y))

        trie = Trie()
        ## O(m * l)
        for word in words:
            trie.insert(word)

        visited = [ [False] * len(board[0]) for _ in range(len(board))]
        cur = []
        res = []
        self.dfs(charIndices, trie.root, None, None, visited, cur, res)

        return res


    def dfs(self, charIndices, node, x, y, visited, cur, res):
        if node.wordEnd and not node.found:
            res.append(''.join(cur))
            node.found = True

        ## at most 26 character
        for c, n in node.children.items():
            if c in charIndices:
                for newX, newY in charIndices[c]:
                    if visited[newX][newY] or not self.isAdj(x, y, newX, newY):
                        continue
                    visited[newX][newY] = True
                    cur.append(c)
                    self.dfs(charIndices, n, newX, newY, visited, cur, res)
                    visited[newX][newY] = False
                    cur.pop()


    def isAdj(self, x, y, newX, newY):
        if x is None or y is None:
            return True

        diffX = newX - x
        diffY = newY - y
        if diffX == 0 and (diffY == -1 or diffY == 1):
            return True

        if diffY == 0 and (diffX == -1 or diffX == 1):
            return True

        return False
        


    @staticmethod
    def main():
        sol = Solution()
        board = [
            ['o','a','a','n'],
            ['e','t','a','e'],
            ['i','h','k','r'],
            ['i','f','l','v']
        ]
        words = ["oath","pea","eat","rain"]
        print(sol.findWords(board, words))


class Solution2(object):
    ## Complexity, board n^2, words: m * l
    ##     O(m * n ^ 2 * (4 ^ l))
    ##   there are m words.  any n^2 character of board could be the starting point
    ##   from each starting point, there are potentially 4 ^ l paths
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if len(board) == 0 or len(board[0]) == 0:
            return []

        charIndices = {}
        for x in range(len(board)):
            for y in range(len(board[0])):
                c = board[x][y]
                if c not in charIndices:
                    charIndices[c] = []
                charIndices[c].append((x, y))

        res = []
        for word in words:
            if self.findWord(board, charIndices, word):
                res.append(word)

        return res


    def findWord(self, board, charIndices, word):
        if not word:
            return True
        
        beginChar = word[0]
        visited = [ [False] * len(board[0]) for _ in range(len(board))]
        if beginChar in charIndices:
            for x, y in charIndices[beginChar]:
                if self.dfs(board, x, y, word, 1, visited):
                    return True

        return False


    def dfs(self, board, x, y, word, idx, visited):
        if idx == len(word):
            return True
        
        visited[x][y] = True
            
        c = word[idx]
        for dx, dy in [(-1,0), (1, 0), (0, -1), (0, 1)]:
            newX = x + dx
            newY = y + dy
            if newX >= 0 and newX < len(board) and newY >= 0 and newY < len(board[0]):
                cur = board[newX][newY]
                if cur == c and not visited[newX][newY] and self.dfs(board, newX, newY, word, idx + 1, visited):
                    visited[x][y] = False
                    return True

        visited[x][y] = False

        return False


    @staticmethod
    def main():
        sol = Solution()
        board = [
            ['a', 'a']
        ]
        words = ["aaa"]
        print(sol.findWords(board, words))

if __name__ == "__main__":
    Solution.main()

