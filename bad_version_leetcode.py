# given a number , find which is the bad number in this you only able to see the n th number which is input for example n = 41 that means it is from 0 to 41 and 
# bad number is hidden in this i fiond the bad number and return this bad number with the minimum calls a function is given to me that is boolean i call this if the version is bad 
# try to find and return bad number with the minimum calls a bad verion (number) can cause to defect all of the next versions

# for example n = 5
# 4 (bad version hide for me) 

def bad_version(version : bool):
    if version == 11:
        return True



def find_version(n):
    for i in range(0, n+1):
        if bad_version(i):
            return i 
        

n = 16
fv = find_version(n) 
b = bad_version(11)