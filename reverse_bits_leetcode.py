# given a 32 bits of integer, reverse this 32 bits and change this into the integer real value 
# for example input = 0,0,0,0,1,0,0,1,1,1,1,1,1,0,0,0,0,1,0,1,1,0,0,1,1,1,1,0,0,0, 
# output = 964176192 (0,0,0,1,1,1,1,0,0,1,1,0,1,0,0,0,0,1,1,1,1,1,1,1,0,0,1,0,0,0,0), (when reversing bits then there answer is this when change this reverse bits into the integer) 


def reverse_bits(n: int):
    r = 0 
    p = 31 
    while (n > 0):
        r += (n&1) << p
        n = n >> 1
        p -= 1 
    return r
    



n = 0b11100011110110100100000001100100
rb = reverse_bits(n)
print(rb)