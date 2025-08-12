# implement a first in first out FIFO queue using the stacks, make a operations like (push, peek, pop, empty)
# push (insert the element in the stack)
# pop (delete the element into the stack)
# peek (first element in the stack)
# empty (is the stack have no elements)

class Queue_Stack:
    def __init__(self):
        self.queue_in = []
        self.queue_out = []


    def push(self, val):
        self.queue_in.append(val) 




    def pop(self):
        if not self.queue_out:
            while self.queue_in:
                self.queue_out.append(self.queue_in.pop())
        return self.queue_out.pop()


    
    def peek(self):
        if not self.queue_out:
            while self.queue_in: 
                self.queue_out.append(self.queue_in.pop())

        return self.queue_out[-1]


    
    def empty(self):
        if (len(self.queue_in)) == 0 and (len(self.queue_out)) == 0:
            return True 
        

        else:
            return False 
        



qs = Queue_Stack()
qs.push(4)
qs.push(8)
qs.pop()
p = qs.peek()
e = qs.empty()

print(qs.queue_out) 


# another way to do that 


class Queue_Sk:
    def __init__(self):
        self.stk1 = []
        self.stk2 = []


    def push(self, val):
        self.stk1.append(val)


    def pop(self):
        for _ in range(len(self.stk1)):
            self.stk2.append(self.stk1.pop(-1))

        poped = self.stk2.pop(-1)

        for _ in range(len(self.stk2)):
            self.stk1.append(self.stk2.pop(-1))

        return poped 
    

    def peek(self):
        for _ in range(len(self.stk1)):
            self.stk2.append(self.stk1.pop(-1))

        pek = self.stk2[-1]

        for _ in range(len(self.stk2)):
            self.stk1.append(self.stk2.pop(-1))
        return pek 
    

    def empty(self):
        if len(self.stk1) == 0:
            return True 
        

        else:
            return False 
        

qt = Queue_Sk()
qt.push(14)
qt.push(4)

qt.pop()

t = qt.peek()

e = qt.empty()

print(qt.stk1)
print(t)
print(e)