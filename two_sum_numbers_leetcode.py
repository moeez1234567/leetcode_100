# twosum numbers in the given list you have add 2 numbers that can match the target number list = [2,4,6,9], target = 11 dont duplicate 2 indexes
# number = [5,4,3,9]
# target = 12


def twonum(number, target):
    for i in range(len(number)):
        required = target - number[i]
        if (required in number) and (number.index(required) != i):
            return [i, number.index(required)]
        

tw = twonum([5,4,3,9],12)
print(tw)



# most effecient method to write this code use dict
def twosum(number, target):
    d = dict()
    for i in range(len(number)):
        d[number[i]] = i
    for i in range(len(number)):
        required = target - number[i]
        if (required in d.keys()) and (d[required]) != i:
            return [i, d[required]]
        

dn = twosum([5,4,3,6], 7)
print(dn)