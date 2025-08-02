# given an integers array retrun the number which appears more times in the list and this number must be appear [ln/2] times in the list means that half times 
# for example nums = [3,2,3]
# output = 3 (because 3 is appears more times in the list)

# input = [2,2,1,1,2,2]
# output = 2 (because 2 is appear more times in this list)


def majority_element(nums : list):
    max_num = len(nums) // 2 
    for num in nums:
        n_times = [1 for elem in nums if elem == num]
        if n_times > max_num:
            return num 
        
    


nums = [2,2,1,1,2,2]
me = majority_element(nums)