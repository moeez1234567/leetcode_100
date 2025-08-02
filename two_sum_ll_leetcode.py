# given a integer array with the target array is sorted in the ascending order , the target is equals to the sum of 2 numbers in the sorted list you return where is this numbers that we can 
# add in the sorted array to reach the target value return their numbers indexes and dont use duplicate numbers and also return indexes in the 1 not start from 0
# for example input = [2,4,5,8,9,11] , target = 12 





def find_numbers_target(array : list, target : int):
    for i in array:
        required = target - i
        if required in array and i != required:
            a , b =   array.index(i), array.index(required)
            return a +1, b+1 



array = [2,4,5,8,9,11]
target = 12
fnt = find_numbers_target(array, target)
print(fnt) 




# another way
def two_sum_numbers(array : list, target : int):
    for i in array:
        for j in array[::-1]:
            if i + j == target and i != j:
                a,b = array.index(i), array.index(j)

                return a+1, b+1


array = [2,4,5,7,11]
target = 12
tsn = two_sum_numbers(array, target)
print(tsn)




# another way to do that 
def find_sum_target(array: list, target:int):
    left = 0
    right = len(array) -1 

    while (left < right):
        req = array[left] + array[right]
        if req > target:
            right -= 1
        elif req < target:
            left += 1 

        else:
            a,b = array.index(array[left]) , array.index(array[right]) 
            return a+1, b+1



array = [2,4,5,7,11]
target = 11
fst = find_sum_target(array, target)
print(fst)