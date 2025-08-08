# Given 2 sorted arrays of nums1 and the nums2 , merge nums2 in the nums1 array and return sorted array , the nums1 length makes the double because of m+n which represent the length od the nums1 and nums2 length 
# 
# example  nums1 = [123000], nums2 = [678]
# output = [123678]

# nums1 = [1], nums2 = []
# output = 1 



def merge_sorted_list(nums1 : list ,m, nums2 : list, n):
    last = m + n -1 

    while (m > 0 and n > 0):
        if nums1[m - 1] > nums2[n - 1]:
            nums1[last] = nums1[m - 1]
            m -= 1 
        else:
            nums1[last] = nums2[n - 1]
            n -= 1 

        last -= 1 

    while n > 0:
        nums1[last] = nums2[n - 1]
        n , last = n - 1, last - 1 

    return nums1 


  

msl = merge_sorted_list(nums1 = [1,2,3,0,0,0],m = 3,nums2 = [5,7,9], n = 3)
print(msl)