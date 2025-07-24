# Given a non negative integer, return their square root , only include the decimal value means return the square root only the part which is before the point 
# for example x = 4 
# output 2 

# x = 5 
# output = 2 

import math 

def square_root(x : int):
    sq = math.sqrt(x)
    return int(sq)
     


sr = square_root(12) 
print(sr)


# Another Approch without importing Math
def squareroot(x : int):
    return int(x**0.5) 


sroot = squareroot(15)
print(sroot)