# given an array integers and the number digit, return True if the 2 duplicate values in the array in which indexes calculte their indexes difference and
#  check if the distance between 2 indexes are less then to the single input digit or the equals then return the True  and if the distance between 2 indexes are greater then the given value
#  then returns the false 
# for example input = [1,2,3,1], k = 3
# output = Ture (because duplicate in this array are 1 and 1 first 1 is the 0th index and the other one is the 3 index when we calculate them then it makes value equals to the 3 which is equals to input)


def duplicate_sum(array : list, k : int): 
    seen = set()
    for a in array:
        if a in seen:
                ass = array.index(a)
                print(ass)
                array.pop(ass)
                for b in array:
                    if b == a:
                        ib = array.index(b)
                        ib += 1
                        print(ib) 
                        if ass + ib <= k:
                             return True
        else:
            seen.add(a) 


    return False        
     

array = [14,12,13,14,15]
k = 14

ds = duplicate_sum(array, k)
print(ds) 

# correct approch 
def distance_duplicates(array : list, k:int):
    index_dict = {}
    for i,num in enumerate(array):
        if num in index_dict and i - index_dict[num] <= k:

            return True 

        else:
            index_dict[num] = i 

    
    return False 


array = [2,5,8,5]
k = 2
dd = distance_duplicates(array, k)
print(dd)


        

# another way to do that 
def distance_indexes(array:list, k:int):
    for i in range(len(array)):
        for j in range(len(array)):
            if i == j:
                continue
            if array[i] == array[j] and abs(i - j) <= k:
                return True 
            
    else:
        return False 
    

array = [2,5,8,5]
k = 2
di = distance_indexes(array, k)
print(di)
