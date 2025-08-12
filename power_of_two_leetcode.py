# given a integer number, return true if it is the power of 2 like 16 is the 2^4 return true and 1 is the 2^0 2 powers 0 so its true 5 is not the power of 2 and same like 3 
# 
# input = 10
# output = True 
# 
# input = 7
# output = False (because 7 is not in the power of 2)



def power_of_two(num:int):
    b = bin(num).replace("0b","")
    if b.count("1") == 1:
        return True
    
    else:
        return False 


num = 16
pot = power_of_two(16)
print(pot)


# another way to do that

def power_two(num:int):
    if num > 0 and num & num-1 == 0:
        return True 
    else:
        return False 
     

num = 19
pt = power_two(num)
print(pt)