# givena non descending order sorted array , return the square of each number in this array , sort the answer in the non-descending order
# for example input = [-4,-1,0,3,10]
# output = [0,1,9,16,100] (taking the square root of each numer and finish the - sign and then sort their answers in the non-descending order)


def sorted_squares(array : list):
    roots = []
    for i in array:
        r = i ** 2
        roots.append(r) 
    
    roots.sort()

    return roots





array = [-7,-3,2,3,11]
ss = sorted_squares(array)
print(ss) 


# another way to do that
import math

def array_squares(array:list): 
    squares = [i**2 for i in array]
    res = squares[0]
    result = []
    l = 1
    while True:
        if squares[l] < res:
            res = squares[l]

        l += 1 
        if l == len(squares):
            result.append(res)
            squares.remove(res) 
            res = math.inf

            l = 0 

        if len(squares) == 0:
            break 

    return result 
            


array = [-4,-2,-1,4,7,8,9]
ass = array_squares(array)
print(ass)