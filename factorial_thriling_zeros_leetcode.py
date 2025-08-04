# given a int , you can take the factorial of this num like input = 35 ansd their factorial 35 * 34 * 33 and after taking their factorial check how many zeros in their final answer 
# return the final answer zeros like for example factorial of 23 is 23*22*21 2460420 output 2 because 2 zeros in the answer 

# Note : Try to solve this in o(1)

# input = 46 
# output is  


def factorial_thrilig_zeros(n :int):
    result = 1 
    for i in range(1, n+1):
        result *= i 
    
    res = str(result)
    
    zeros = 0
    for r in res[::-1]:
        if r == "0":
            zeros += 1
        else:
            break 

    return zeros



n = 47
ftz = factorial_thrilig_zeros(n)
print(ftz) 


# another easy way to do that 
def trailing_zeros(n: int):
    count = 0
    while (n >= 5):
        n //= 5
        count += n 
    
    return count 



n = 47
tz = trailing_zeros(n)
print(tz)
