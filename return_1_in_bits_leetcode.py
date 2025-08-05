# given a integer of bits 0,1s , return the 1s in this bit 
# for example input = 010101011 
# output = 5 (because 1s arrive 5 times in the bit table (input))



def ones_in_bit(n : int):
    ones = 0 
    while n:
        n &= n - 1
        ones += 1
    
    return ones 

 

n = 10101010010101
oib = ones_in_bit(n)
print(oib) 




# another way to do that
def ones_bit(n:int):
    ones = 0 
    while (n > 0):
        if n & 1 == 1:
            ones += 1 

        n = n >> 1 

    return ones 




n = 10101010010101
ob = ones_bit(n)
print(ob)