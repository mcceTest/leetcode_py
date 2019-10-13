'''
Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
Example 1:

Input:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be",
             because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified becase it contains only one word.
Example 3:

Input:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
'''



class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        
        result = []

        res = []
        lineWordLength = 0

        for word in words:
            if lineWordLength + len(res) + len(word) > maxWidth:
                result.append(self.mergeWords(res, lineWordLength, maxWidth))

                res = []
                lineWordLength = 0
            res.append(word)
            lineWordLength += len(word)

        if res:
            result.append(self.mergeWords(res, lineWordLength, maxWidth, True))

        return result


    def mergeWords(self, res, lineWordLength, maxWidth, isLastLine=False):
        if not isLastLine:
            spaceCount = maxWidth - lineWordLength
            if len(res) == 1:
                return res[0] + ' ' * spaceCount
            else:
                low = spaceCount // (len(res) - 1)
                left = spaceCount - low * (len(res) - 1)
                
                if left == 0:
                    return (' ' * low).join(res)
                else:
                    s = (' ' * (low + 1)).join(res[:(left + 1)])
                    for idx in range(left + 1, len(res)):
                        s += ' ' * low
                        s += res[idx]
                    return s
                    
        else:
            return ' '.join(res) + ' ' * (maxWidth - lineWordLength - len(res) + 1)


    @staticmethod
    def main():
        sol = Solution()
        words = ["ask","not","what","your","country","can","do","for","you","ask","what","you","can","do","for","your","country"]
        maxWidth = 16

        print(sol.fullJustify(words, maxWidth))



if __name__ == "__main__":
    Solution.main() 

