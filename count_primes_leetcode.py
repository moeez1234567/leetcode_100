# given a number integer, return how much prime numbers (prime numbers are those who starts from 2 and  only be divide in their own table not divide into the anoter table is called prime number)
# return their length how many prime numbers came before this given integer 

# for example input = 10 
# output = 4 (because there are 4 prime numbers before 10 2,3,5,7 and their length is 4)\

# input = 1
# output = 0 

def prime_numbers_integer(num):
    numbers = []
    tra = 0
    if num == 3:
        numbers.append(2)
    elif num > 3:
        numbers.append(2)
        numbers.append(3)
    for n in range(2, num):
        if n % 2 == 0 or n % 3 == 0:
            tra += n 
        else:
            numbers.append(n)  
    
    return len(numbers)


num = 12
pni = prime_numbers_integer(num)
print(pni)