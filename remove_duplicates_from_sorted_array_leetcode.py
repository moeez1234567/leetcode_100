# Remove duplicates from the sorted list are return the actual value without duplicates and dont make a new list just work on the existing list 
# for example  input = lt = [2,3,3,4,5,6,6,7,9]
# output = 7,  nums = [2,3,4,5,6,7,9] 

def remove_duplicate(l : list):
    len_l = len(l)
    last = len_l - 1
    start = len(l[1:])
    for i in l:
        if i in l[start: last]:
            duplicate = i 
        if i not in l[start: last]:
            actual_value = i 

        start += 1 

    return duplicate, actual_value
            

        # actual_value = i
        # start = 1
        # for n in start:
        #     if i in l[n:]:
        #         duplicate_valu = i 
        #         return duplicate_valu , actual_value 
    #     print(actual_value)    
    # return actual_value

rd = remove_duplicate([2,3,4,5,5,6])
            


        