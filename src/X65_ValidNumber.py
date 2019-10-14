'''
Validate if a given string can be interpreted as a decimal number.

Some examples:
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

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one. However, here is a list of characters that can be in a valid decimal number:

Numbers 0-9
Exponent - "e"
Positive/negative sign - "+"/"-"
Decimal point - "."
Of course, the context of these characters also matters in the input.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button to reset your code definition.
'''


class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()

        if len(s) == 0:
            return False

        eIdx = -1
        for i, c in enumerate(s):
            if c == ' ':
                return False
            elif c == 'e':
                if eIdx != -1:
                    return False
                else:
                    eIdx = i

        if eIdx == -1:
            return self.isSimpleNumer(s, 0, len(s) - 1)
        else:
            return self.isSimpleNumer(s, 0, eIdx - 1) and self.isSimpleNumer(s, eIdx + 1, len(s) - 1, False, True)

    def isSimpleNumer(self, s, startIdx, endIdx, allowDot=True, needNum=True):
        if startIdx > endIdx:
            return False

        numIdx = -1
        dotFound = False

        for i in range(startIdx, endIdx + 1):
            c = s[i]
            if c == '-' or c == '+':
                if i != startIdx:
                    return False
            elif c == '.':
                if not allowDot:
                    return False

                if dotFound or (numIdx == -1 and i == endIdx):
                    return False
                else:
                    dotFound = True
            elif ord(c) >= ord('0') and ord(c) <= ord('9'):
                if numIdx == -1:
                    numIdx = i
            else:
                return False

        if needNum and numIdx == -1:
            return False
        else:
            return True

    @staticmethod
    def main():
        sol = Solution()
        s = '0'
        print(sol.isNumber(s))
        

if __name__ == "__main__":
    Solution.main() 
            


                
                    

                
