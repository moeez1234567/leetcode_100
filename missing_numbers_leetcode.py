# given a array of nums , return the missing numbers in this array are mix in the list return the number missing from the shortest number to the largest number in the array
# for example input = [2,3,5,0]
# output = [1,4] (because this numbers are missing in this from 0 to 5)
# 
# input = [4,9]
# output = [5,6,7,8] (because 5,6,7,8 are the only numbes thats are missing between the 4 to 9)
# Note : try to do this in o(1) extra space compexity (means without making bnew array and o(n) login time means use only one loop)


def find_missingnumbers(array:list):
    i = 0
    m = 0
    l = []
    s = set(array)
    while (i <= len(array)):
        if m+i not in s: 
            l.append(m+i)  

        i +=1 

    return l


            



array = [0, 1, 2]
fm = find_missingnumbers(array)




# another way to do that 
def missing_numbers(array : list):
    array.sort()
    if array[-1] != len(array):
        return len(array)
    
    if array[0] != 0:
        return 0 
    

    for i in range(1, len(array)):
        if i not in array:
            return i
        

array = [0,1,4,3]
mn = missing_numbers(array)



# another way to do that 
def missing_numbers(array : list):
    s = set(array)
    n = len(array) + 1 
    for i in range(n):
        if i not in s:
            return i 
        

array = [0, 1, 2]
m_num = missing_numbers(array) 


# another way to do that 
def missing_numbers(array : list):
    required = len(array) * (len(array) +1) //2 
    sums = sum(array)
    return required - sums 


array = [0,1,4,3] 
missing_n = missing_numbers(array) 


# another way to do that o(n) time complexity
def missing_number(array : list):
    n = len(array)
    return sum(range(0,n+1)) - sum(array)