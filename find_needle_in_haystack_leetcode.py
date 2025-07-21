# return the index of the needle find in the haystack 2 values are given haystack = "greenlantern" and needle = "ee" like and return the index if find the needle where the needle start in the haystack output = 2
# 
# for example 
# haystack = "seventeen"
# needle = "ven"
#  output = 2 

# haystack = "twelve"
# needle = "ing"
# output = -1 


def find_needle(haystack : str, needle : str):
    return haystack.find(needle) 


fn = find_needle("imbatman", "wrt")
print(fn)



# Another way 
def find_needle_haystack(haystack : str, needle : str):
    if needle == "" or haystack == "  ":
            return 0 
       
    i = 0
    j = 0

    while (i < len(haystack)):
        if haystack[i] in needle[j] and haystack[i+1] in needle[j+1]:
            val = i
            break
        i += 1 

    else:
        return -1 
    


    return val
         


fnh =  find_needle_haystack("muslims", "lims")
print(fnh)




# ANOTHER APPROCH
def find_needle_in_haystack(haystack, needle):
    if needle and haystack == "":
        return 0
    i = 0
    n = len(needle)

    while (i+n <= len(haystack)):
        if haystack[i : i+n] == needle:
            return i 
        i += 1
    else:
        return -1 
     







fnih = find_needle_in_haystack("terabite", "bite")
print(fnih)



