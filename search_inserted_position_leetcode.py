# given a sorted array with no repeated words, and a target value, returns the index of the target value in the sorted array if found else return their suted index where it comes in the sorted order

# for example 
# input = [1,2,3,4,7] , target = 6
# output = 5 

# input = [2,4,5,6] , target = 3
# output = 2 


def search_inserted_position(array : list, target):
    i = 0 
    while (i < len(array)):
        if target == array[i]:
            return i 
        
        i += 1 

    else:
        l = []
        l.extend(array)
        t = [target]
        l.extend(t)
        # fnl = l.sort(l)
        # fnl.index(target)
        l.sort() 
        l.index(target)
        print(l.index(target))
        

        return l










sip = search_inserted_position([1], target=0)
print(sip)



# Another way to do 
def find_inserted_position(array : list, target):
    i = 0
    while (i < len(array) and target >= array[i]):
        if target == array[i]:
            return i 
        i += 1
    
    return i
    









fip = find_inserted_position([2,3,5,6,7,9], 12)
print(fip)