# given a binary array, return how many times 1s arrive continuously in this array return their length
# 
# for example array = [0,1,1,0,1,1,1]
# output = 3 (because 1 are arrive continuously 3 times in this array)


def continuously_ones(array : list):
    max_l = 0
    ones = int()
    for i in array:
        if i == 1:
            ones += 1
        else: 
            if ones > max_l:
                max_l = ones 
                ones = 0
    
    return max_l





array = [1,1,0,0,0,1,1,1,1,0,1,1,1]
co = continuously_ones(array)
print(co)