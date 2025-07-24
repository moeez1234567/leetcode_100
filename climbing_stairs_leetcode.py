# given a stairs with the number n target stairs where you can reacj and you have the 2 ways to climb by the taking 1 step or 2 step you retrun that from how much ways to climb into this stairs 
# by taking 1 and 2 steps 

# for example n = 4 
# output = 5 


def climbing_stairs(n : int):
    if n < 2:
        return n 

    a , b = 1,2 
    for _ in range(3, n+1):
        a , b = b , a+b 

    return b 




c_s = climbing_stairs(27)
print(c_s) 




# 
def climb_stairs(n):
    one = 1 
    two = 1 

    for i in range(n - 1):
        temp = one 
        one = one + two 
        two = temp 


    return one 






cs = climb_stairs(13)