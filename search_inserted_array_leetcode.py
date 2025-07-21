# given a sorted array with no repeated words, and a target value returns the index of the target value in the sorted array if found else return their suted index

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
      fnl = l.sort(l)
        # fnl.index(target)

        return fnl










sip = search_inserted_position([1,3,5,7], target=2)
print(sip)