# given a list of integers all the numbers are duplicate except one find this number which is alone dont duplicate and then return 
# Note: implement a solution with a linear runtime complexity and without using extra memory 

# input = [2,2,1]
# output = 1 

# nums = [4,1,2,1,2] 
from collections import Counter


def single_number(nums : list):
    counter = Counter(nums)
    for num, count in counter.items():
        if count == 1:
            return f"{num} apperas in the {count} times"


nums = [1,2,1]
sn = single_number(nums)
print(sn) 



# another way to do that 
def find_single_number(nums : list):
    n = 0 
    l = []
    while (n < len(nums)): 
        if nums[n] not in l:
            l.append(nums[n])   
        else:
            l.remove(n)

        n += 1 

    return l


nums = [3,4,5,3,4]
fsn = find_single_number(nums)
print(fsn)




# another best way to do that
def single_number_find(nums:list):
    return [2 * sum(set(nums)) - sum(nums)] 


nums = [3,4,5,3,4]
snl = single_number_find(nums)
print(snl)