import unittest

from X65_ValidNumber import Solution

'''
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false
'''

class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()

        examples = '''
                    "0" => true
                    " 0.1 " => true
                    "abc" => false
                    "1 a" => false
                    "2e10" => true
                    " -90e3   " => true
                    " 1e" => false
                    "e3" => false
                    " 6e-1" => true
                    " 99e2.5 " => false
                    "53.5e93" => true
                    " --6 " => false
                    "-+3" => false
                    "95a54e53" => false
                    '''
        for line in examples.strip().split('\n'):
            fields = line.strip().split('=>')
            s = fields[0].strip().strip('"')
            ep = (fields[1].strip() == 'true')

            print("s:[{0}], ep:[{1}]".format(s, ep))
            if ep:
                self.assertTrue(sol.isNumber(s))
            else:
                self.assertFalse(sol.isNumber(s))

    def test2(self):
        sol = Solution()
        s = "3."
        self.assertTrue(sol.isNumber(s))

    def test3(self):
        sol = Solution()
        s = "."
        self.assertFalse(sol.isNumber(s))


    def test4(self):
        sol = Solution()
        s = "4e+"
        self.assertFalse(sol.isNumber(s))

       
if __name__ == "__main__":
    unittest.main()