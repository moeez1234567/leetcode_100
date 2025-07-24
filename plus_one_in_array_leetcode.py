# given a array of decimal numbers , this numbers are single in the array , not a negative value ,
#   dont start with the 0 however 0 comes in the middele itself , add 1 in this full array value and first integer is the head of the array

# example array = [3,4,5,0,7]
# output = 34508

# example array = [0]
# output = 1


def add_one(array: list):
    integer = int("".join([str(a) for a in array]))
    integer += 1
    back = str(integer)

    arr = list(int(b) for b in back) 
    return arr


ao = add_one([3, 4, 5, 0, 9])
print(ao)
