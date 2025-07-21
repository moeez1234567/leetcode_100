# given a array of numbers you can remove the instance that provided from this array and return the length after removing this instance 
# Note : dont allocate extra array works in the input array dont create another array

# for example arr = [2,3,4,4], val = [4,2]
# output = [3] , its length 1 

def remove_element(arr : list,  val):
    i = 0
    l = len(arr)
    l = l-1
    while (i < l):
        if arr[i] == val:
            arr.pop(i)
            
        
        i += 1
    print(arr)
    print(len(arr))
    return arr 
    

re = remove_element([2,3,4,5,6], 5)
print(re)


# # ANOTHER WAY TO DO THIS 
# def remove_dup(arr : list, val):
#     i = 0
#     while (i < len(arr)):
#         if arr[i] == val:
#             arr[i], arr[-1] = arr[-1], arr[i]
#             arr.pop(i)
        
#         i += 1
         
#     print(arr)
#     return len(arr), arr 
    

# remove_d = remove_dup([3,4,5,5,6,6,7], 6)
# print(remove_d)