# make a stack like a dustbin in this stack several function will be able to perform like remove , pop , append, duplicate, retrive minimum element in constant time, top

# for example input = ["MinStack", "push","push","getMin","pop","top","getMin"]


class Stack:
    def __init__(self):
        self.stk = []
        self.min_stack = []


    def push(self, val: int):
        self.stk.append(val) 
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self):
        self.stk.pop()
        self.min_stack.pop()


    def top(self):
        return self.stk[-1]

    def getMin(self):
        return self.min_stack[-1]
    

    


s = Stack()
s.push(3)
s.push(9)
s.pop()
# s.push(-1)

m = s.getMin()
t = s.top()

print(s.stk)
print("min val", m)
print("top val", t)


