# given an integers array retrun the number which appears more times in the list and this number must be appear [ln/2] times in the list means that half times 
# for example nums = [3,2,3]
# output = 3 (because 3 is appears more times in the list)

# input = [2,2,1,1,2,2]
# output = 2 (because 2 is appear more times in this list)


def majority_element(nums : list):
    max_num = len(nums) // 2 
    for num in nums:
        n_times = [num for elem in nums if elem == num]
        if len(n_times) > max_num:
            return num 
        
    


nums = [2,2,1,1,2,2,1,1,1]
me = majority_element(nums)
print(me) 



# another way to do
def max_element(nums):
    d = dict()
    for n in nums:
        if n not in d.keys():
            d[n] = 1 
        else:
            d[n] = d[n] + 1

    
    times_a = 0
    ans = 0
    for n in nums:
        if d[n] > times_a:
            times_a = d[n]
            ans = n 

    return f"{ans} appears {times_a} times"


nums = [3,4,5,6,6,4,4,4,4]
m_e = max_element(nums)
print(m_e) 




from collections import Counter
# with collections 
def m_elements(nums):
    max_n = Counter(nums)
    return max(max_n.keys(), key = max_n.get)


nums = [3,4,5,6,6,4,4,4,4]
m_el = m_elements(nums)
print(m_el)
