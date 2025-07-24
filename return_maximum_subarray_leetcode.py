# given a contiguous array means index attach to each other return the maximum subarray(only 1) in this list and + plus this maximum subarrays and return their value
# for example nums = [-2,1,-3,4,-1,2,1,-5,4]
# output = 6
# explanation [4,-1, 2,1] has the largest sum 6
import math


def return_maximum_subarray(array: list):
    i = 0
    if len(array) > 0:
        j = 1
    else:
        return array
    # i = 0
    # # j = 1
    if len(array) > 1:
        i = 0
        j = 1
        
        lst2 = []
        while(i < len(array) and j < len(array)): 
            val2 = array[i] + array[j]
            lst2.append(val2)
            i += 1 
            j += 1 
        value2 = max(lst2)
    
    if len(array) > 2:
        i = 0
        j = 1 
        k = 2  


        lst3 = []

        while (i < len(array) and j < len(array) and k < len(array)):
            val3 = array[i] + array[j] + array[k]
            lst3.append(val3) 
            i += 1
            j += 1
            k += 1 

        value3 = max(lst3) 




    if len(array) > 3:
        i = 0
        j = 1 
        k = 2
        l = 3  


        lst4 = []

        while (i < len(array) and j < len(array) and k < len(array) and l < len(array)):
            val4 = array[i] + array[j] + array[k] + array[l]
            lst4.append(val4) 
            i += 1
            j += 1
            k += 1 
            l += 1

        value4 = max(lst4)



    if value2 > value3 and value4:
        return value2 
    
    if value3 > value2 and value4:
        return value3 

    if value4 > value3 and value3:
        return value4 
    
    else:
        ("go to hell")

    # if value3 > val2 and value1:
    #     return value3   
    
    # else:
    #     lst3





rms = return_maximum_subarray([1, 2, -4, -1, -6, -1])
print(rms)



# Another Way 

def find_maximum_subarray(array : list):
    maximum_array = -math.inf
    for i in range(len(array)):
        current_values = 0
        for j in range(i, len(array)):
            current_values += array[j]

            maximum_array = max(current_values, maximum_array)

    return maximum_array
     












fms = find_maximum_subarray([-4,-2,-1,4,5,-2])
print(fms)



# Another way to do that 
def maximum_subarray(array : list):
    current_array = array[0] 
    maximum_array = array[0]

    for arr in array[1:]:
        current_array = max(arr, current_array + arr)
        maximum_array = max(current_array, maximum_array)


    return maximum_array 











ms = maximum_subarray([-2,-4,1,5,-3,-2])
print(ms)