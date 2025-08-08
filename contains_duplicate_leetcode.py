# given a array < return if any number appears 2 times in this array then return True , if no number is duplicate then return the False 
# for example input = [1,2,3,1]
# output = True (because the 1 appears 2 times in this array(list))
# input = [1,2,3,4]
# output = False (because none of the number is appears 2 times)

def contains_duplicate(array): 
    l = []
    for i in array:
        if i not in l:
            l.append(i)
        else:
            return True 
    
    return False


array = [7,5,3,3,1,2]
cd = contains_duplicate(array)
print(cd)

# this approch takes the o(n2) times which is too long so ths is not good for the seeing the leetcode problem 




# better approch
def contain_duplicate(array):
    seen = set()
    for r in array:
        if r in seen:
            return True 
        else:
            seen.add(r)  
    return False


array = [5,6,7,8,9,9]
c_d = contain_duplicate(array)
print(c_d)
