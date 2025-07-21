# Remove duplicates from the sorted list are return the actual value without duplicates and dont make a new list just work on the existing list 
# for example  input = lt = [2,3,3,4,5,6,6,7,9]
# output = 7,  nums = [2,3,4,5,6,7,9] 

def remove_duplicate(l : list):
    i = 0 
    while (i < len(l)):
        j = i + 1
        while (j < len(l) and l[i] == l[j]):
            l.pop(j)
            print(l)

        i = j 

    return  l


rd = remove_duplicate([2,3,4,5,5,6])
            
