'''
You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input:
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
Output: []
'''


## TODO: Try to start from every possible index in s and see if all the words can be used to match a substring

class Solution(object):
    def findSubstring2(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        words = list(filter(lambda word: word, words))
        totalWordLength = 0
        for word in words:
            totalWordLength += len(word)

        if not words or totalWordLength > len(s):
            return []

        wordIdxMap = {}
        wordIdxCount = []
        wordLengths = []
        idxMap = {}
        curIdx = 0
        for word in words:
            if word not in wordIdxMap:
                wordIdxMap[word] = curIdx
                wordIdxCount.append(1)
                wordLengths.append(len(word))

                indices = self.findAll(s, word)
                if indices:
                    for idx in indices:
                        if idx not in idxMap:
                            idxMap[idx] = []
                        idxMap[idx].append(curIdx)
                else:
                    return []

                curIdx += 1
            else:
                wordIdxCount[wordIdxMap[word]] += 1


        totalWords = len(words)

        startPos = sorted(idxMap.keys())
        print(idxMap)
        
        res = []
        for startIdx in startPos:
            # wordsUsed = [False] * totalWords
            useCount = 0
            if self.dfs(startIdx, wordIdxCount, useCount, idxMap, wordLengths, totalWords):
                res.append(startIdx)

        return res
    

    class State(object):
        def __init__(self, idx, useCount, wordsUsed):
            self.idx = idx
            self.useCount = useCount
            
            self.wordsUsed = wordsUsed


    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        words = list(filter(lambda word: word, words))
        totalWordLength = 0
        for word in words:
            totalWordLength += len(word)

        if not words or totalWordLength > len(s):
            return []

        wordIdxMap = {}
        wordIdxCount = []
        wordLengths = []
        idxMap = {}
        curIdx = 0
        for word in words:
            if word not in wordIdxMap:
                wordIdxMap[word] = curIdx
                wordIdxCount.append(1)
                wordLengths.append(len(word))

                indices = self.findAll(s, word)
                if indices:
                    for idx in indices:
                        if idx not in idxMap:
                            idxMap[idx] = []
                        idxMap[idx].append(curIdx)
                else:
                    return []

                curIdx += 1
            else:
                wordIdxCount[wordIdxMap[word]] += 1


        totalWords = len(words)

        startPos = sorted(idxMap.keys())
        startPos = filter(lambda x: x + totalWordLength <= len(s), startPos)
        print(idxMap)
        
        res = []
        for startIdx in startPos:
            # wordsUsed = [False] * totalWords
            useCount = 0
            st = []
            state = self.State(startIdx, 0, wordIdxCount[:])
            st.append(state)

            while len(st) > 0:
                topElem = st.pop(-1)
                if topElem.useCount == totalWords:
                    res.append(startIdx)
                    break

                if topElem.idx not in idxMap:
                    continue

                for wordIdx in idxMap[topElem.idx]:
                    if topElem.wordsUsed[wordIdx] > 0 and topElem.idx + wordLengths[wordIdx] <= len(s):
                        tmpUsed = topElem.wordsUsed[:]
                        tmpUsed[wordIdx] -= 1
                        st.append(self.State(topElem.idx + wordLengths[wordIdx], topElem.useCount + 1, tmpUsed))

        return res





    def findAll(self, s, word):
        res = []
        idx = 0
        while idx < len(s):
            idx = s.find(word, idx)
            if idx >= 0:
                res.append(idx)
                idx += 1
            else:
                break

        return res


    def dfs(self, idx, wordIdxCount, useCount, idxMap, wordLengths, totalWords):
        if useCount == totalWords:
            return True

        if idx not in idxMap:
            return False

        for wordIdx in idxMap[idx]:
            if wordIdxCount[wordIdx] > 0:
                wordIdxCount[wordIdx] -= 1
                useCount += 1

                nextStepSuccess = self.dfs(idx + wordLengths[wordIdx], wordIdxCount, useCount, idxMap, wordLengths, totalWords)

                wordIdxCount[wordIdx] += 1
                useCount -= 1

                if nextStepSuccess:
                    return True

        return False
                

    @staticmethod
    def main():
        sol = Solution()

        # s = "barfoothefoobarman"
        # words = ["foo","bar"]

        # res = sol.findSubstring(s, words)
        
        # print(res)


        # s = "wordgoodgoodgoodbestword"
        # words = ["word","good","best","word"]
        # print(sol.findSubstring(s, words))

        s = "abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab"
        words = ["ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba"]
        # s = "aaaaaaaa"
        # words =["aa","aa","aa"]

        print(len(s))
        print(len(words))
        print(sol.findSubstring(s, words))


if __name__ == "__main__":
    Solution.main()  