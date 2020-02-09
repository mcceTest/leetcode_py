'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 

Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
'''


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.st = []
        self.mk = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.st.append(x)
        if not self.mk or x <= self.mk[-1]:
            self.mk.append(x)
            
        

    def pop(self):
        """
        :rtype: None
        """
        top = self.st.pop(-1)
        if top == self.mk[-1]:
            self.mk.pop(-1)
        

    def top(self):
        """
        :rtype: int
        """
        return self.st[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.mk[-1]



    @staticmethod
    def main():
        sol = MinStack()
        sol.push(-2)
        sol.push(-3)
        sol.push(0)
        print(sol.getMin())

        sol.pop()
        print(sol.top())
        print(sol.getMin())

        sol.pop()
        print(sol.getMin())


if __name__ == "__main__":
    MinStack.main()
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()