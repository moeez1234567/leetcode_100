# given a number integer check if the number is coming in the prime number then it is a ugly number like in case of 8 which is (2*2*2) 2 is a prime number so this number is a ugly number 
# number if it all factors  comes in the (2,3,5) is a ugly number
# 
# for example input = 14 
# output = False (because 14 is not an ugly number their factors are 2*7 so 7 comes in this thats why it is not a ugly number)



def number_factors(num : int):
    while True:
        if num % 2 == 0:
            num = num // 2 
        elif num % 3 == 0:
            num = num // 3 
        elif num % 5 == 0:
            num = num // 5 
        elif num == 1:
            return True
        else:
            return False 

num = 8
nf = number_factors(num) 





# another way to do that 
def ugly_number(num:int): 
    if num <= 0:
        return False
    for x in [2,3,5]:
        while num % x == 0:
            num = num // x 
        
    
    if num == 1:
        return True 
    else:
        return False


num = 18
un = ugly_number(num)
