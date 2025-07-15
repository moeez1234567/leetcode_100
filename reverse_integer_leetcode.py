#Given a 32bit integer value reverse this value if the input is coming above then 32bit like a = 345 or more then return reverse values in 32bit 
# LIKE x = 12
# output = 21 

# y = -64 
# output = -46  

# z = 678 
#output = 87



def reverse_integer(x):
    if x > 1:
        sign = 1
    else:
        sign = -1

    ab = abs(x)
    st = str(ab)
    rs = st[::-1]
    st_i = sign * int(rs)
    if -2**31 <= st_i <= 2**31 -1:
        return st_i 
    else:
        return 0



es = reverse_integer(-92)
print(es)

