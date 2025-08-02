# given a integer of number gives what its column value 
# for example input 5
# E

# 1
# A

# 2147483627 
# FXSHRXW (because thier integer value converted into the alphabatic chracter makes this FXSHRXM)
def div(val, d):
    a = val // d
    b = val % d

    return a,b

def excel_sheet_column(nums: int):
    result = ""
    while (nums > 0):
        nums -= 1

        q,r = div(nums, 26)
        result = chr(97 + r) + result
        nums = q
        
    return result


num =  197
esc = excel_sheet_column(num)
print(esc) 


# another way to do that 

def num_to_alphabet(num : int):
    number_list = [chr(x) for x in range(ord("A"), ord("Z")+1)]
    print(number_list)
    result = []
    while num > 0:
        result.append(number_list[(num -1 ) % 26] )
        num = (num -1) // 26

    result.reverse()


    return "".join(result)


num = 714
nta = num_to_alphabet(num)
print(nta)

