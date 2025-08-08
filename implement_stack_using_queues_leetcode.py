# make a stack of LIFO 
# (Last in Fast out like arranging plates first there are 1st plate which are keep to the table and then the others but when we picks this plates then we can carry
#  the plate which we can recently added on the top of the all plates that makes the last in which is our first plate and in the last [plate which we can arrange on the top of other plates are
# out first) make a stack operations of LIFO like the push, pop , top, insert  
#  for example input = push[2],pop(),top,push[4],push[5],empty() 
# stack is make like that output = [4,5]

from collections import deque

class MyStack:
    def __init__(self):
        self.deque = deque()

    def push(self,val):
        self.deque.append(val)


    def pop(self):
        self.deque.popleft()
       

    def top(self):
        return self.deque[0]
   

    def empty(self):
        if len(self.deque) == 0:
            return True 
        else:
            return False 




st = MyStack()
st.push(4)
st.pop()
st.push(5)
# st.pop()
t = st.top()
e = st.empty()
print(st.deque)
print(e)
print(t)

