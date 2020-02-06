'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
Example 1:

Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation: 
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

'''


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        st = []
        operators = ('-', '+', '*', '/')
        for s in tokens:
            if s in operators:
                op1 = st.pop(-1)
                op2 = st.pop(-1)

                if s == '-':
                    st.append(op2 - op1)
                elif s == '+':
                    st.append(op2 + op1)
                elif s == '*':
                    st.append(op2 * op1)
                else:
                    res = op2 // op1
                    if res < 0 and res * op1 != op2:
                        res += 1
                    st.append(res)
            else:
                st.append(int(s))

        if st:
            return st.pop(-1)
        return 0 

    @staticmethod
    def main():
        sol = Solution()
        tokens = ["4","-2","/","2","-3","-","-"]
        print(sol.evalRPN(tokens))

if __name__ == "__main__":
    Solution.main()
        