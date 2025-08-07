# given a number integer, return how much prime numbers (prime numbers are those who starts from 2 and  only be divide in their own table not divide into the anoter table is called prime number)
# return their length how many prime numbers came before this given integer 

# for example input = 10 
# output = 4 (because there are 4 prime numbers before 10 2,3,5,7 and their length is 4)\

# input = 1
# output = 0 

def prime_numbers_integer(num):
    t = [True]*num 
    if num < 2:
        return 0 
    t[0], t[1] = False, False
    
    i = 2
    while (i < num):
        if t[i] == True:
            for j in range(i*2,num,i):
                t[j] = False 
        i += 1 

    return t.count(True)

num = 12
pni = prime_numbers_integer(num)
print(pni)