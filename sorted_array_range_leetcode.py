# given a sorted array, chack the continues numbers in this like in the array 0,1,2,4 in there 0 and 2 are continumes and there is missing 3 so its
#  summary is like 0 to 2 and 4 which is there ouytput 

# input = [1,2,3,5,6,7,9]
# output = ["1->3""5->7""9"]



def summary_ranges(array : list):
    if len(array) == 0:
        return None 
    if len(array) == 1:
        return array

    i = 0 
    output = ""
    v = ""
    # cl = ""
    o = []
    j = 0
    while (len(array) != 0):
        # while True:
        #     if j + 1 == len(array):
        #         output = str(array[j])
        #         o.append(output)
        #         break
        #     if array[j] + 1 == array[j+1]:
        #         l.append(array[j])
        #         l.append(array[j+1])
        
        #         j += 1 
        cl = []
        cl += [val for val in range(0, len(array) -1) if array[val]+1 == array[val+1]] 

        # if not cl:
        #     break 


        

        for _ in cl:
            po = array.pop(0) 
            output += str(po)
          
            # cl.clear()
            # break
        #     print(po)
        
        # cl.clear() 
        # v += output[0] + "->" + output[-1]


        o.append(v)

        # i += 1

        output = ""
        # V = ""
        cl = []

        
                
        # else:
    #         if len(l) == 2:
    #             output +=  str(l[0]) + "->" + str(l[1])
    #             l.clear()
    #             o.append(output)
    #             output = "" 
    #         else:
    #             if array[j]+1 != array[j+1]:
    #                 output = str(array[j])
    #                 o.append(output)
    #                 output = "" 
    #                 j += 1
    #     j += 1
    #     i += 1 

    #     # if not array[i + 1]:
    #     #     break 
    # return o



# array = [5,6,8,9,11,13]
# s = summary_ranges(array)



# accurate way to do that
def summary_range(array:list):
    o = []
    while array:
        start = array[0]


        while len(array) > 1 and array[0] + 1 == array[1]:
            array.pop(0)

        end = array.pop(0)


        if start != end:
            o.append(f"{start}->{end}") 

        else:
            o.append(str(start))

    return o 



array = [5,6,8,9,11,13]
s = summary_range(array)
print(s) 


# another way to do that 
def sumary_range(nums : list):
    result = []
    if len(nums) < 1:
        return None
    if len(nums) == 1:
        return nums 
    
    i = 0 
    while i < len(nums):
        j = i + 1
        while j < len(nums):
            if nums[j-1] + 1== nums[j]:
                j+=1 
            else:
                break 

        
        if (j-i) == 1:
            result.append(str(nums[i]))

        else:
            result.append(str(nums[i]) + "->" + str(nums[j-1]))

        
        i = j 

    return result 

nums = [1,2,3,5,6,7,9]
sr = sumary_range(nums)
print(sr)
