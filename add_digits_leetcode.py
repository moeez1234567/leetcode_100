# given a integer number , add its single digit values like 34 3+4 and so on until it reachs to the single value 
# input = 39 
# output = 3 (becaues 3+9 -> 12, 1+2 -> 3 output is a 3 which is the single value) 

def sum_digits(num : int): 

    if num < 10:
        return num 
    output = int()
    while num > 10:
        s = "".join(str(num))
        plus = [int(i) for i in s]
        for i in plus:
            output += i 
        num = output 
        output = 0
        
    return num 
    




num = 14765
sd = sum_digits(num)
print(sd)


# another way to do that 
def add_digits(num : int):
    smm = int()
    for i in str(num):
        smm += int(i)
    
    return smm 




def sums(num:int):
    while len(str(num)) != 1:
        num = add_digits(num)  
    return num 


num = 1456
s = sums(num)
print(s)