import unittest

from X68_TextJustification import Solution

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        words = ["This", "is", "an", "example", "of", "text", "justification."]
        maxWidth = 16   

        self.assertListEqual(sol.fullJustify(words, maxWidth), [
                                                                "This    is    an",
                                                                "example  of text",
                                                                "justification.  "
                                                                ])

    def test2(self):
        sol = Solution()
        words = ["What","must","be","acknowledgment","shall","be"]
        maxWidth = 16 

        self.assertListEqual(sol.fullJustify(words, maxWidth), [
                                                                "What   must   be",
                                                                "acknowledgment  ",
                                                                "shall be        "
                                                                ])


    def test3(self):
        sol = Solution()
        words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
        maxWidth = 20

        self.assertListEqual(sol.fullJustify(words, maxWidth), [
                                                                "Science  is  what we",
                                                                "understand      well",
                                                                "enough to explain to",
                                                                "a  computer.  Art is",
                                                                "everything  else  we",
                                                                "do                  "
                                                                ])


    def test4(self):
        sol = Solution()
        words = ["Science"]
        maxWidth = 20

        self.assertListEqual(sol.fullJustify(words, maxWidth), [
                                                                "Science             ",
                                                                
                                                                ])
    

    def test5(self):
        sol = Solution()
        words = ["ask","not","what","your","country","can","do","for","you","ask","what","you","can","do","for","your","country"]
        maxWidth = 16


        self.assertListEqual(sol.fullJustify(words, maxWidth), [
                                                                "ask   not   what",
                                                                "your country can",
                                                                "do  for  you ask",
                                                                "what  you can do",
                                                                "for your country"])
       
if __name__ == "__main__":
    unittest.main()