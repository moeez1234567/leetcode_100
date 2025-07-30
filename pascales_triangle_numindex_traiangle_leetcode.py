# given a number index return the row of pascales traiangle at this index
# for example rowindex = 3 
# output [1,3,3,1]

# input rowindex = 0
# output = [1]

# input rowindex = 1
# output = [1,1] 


def pascales_traiangle_index(numindex):
    l = []
    for i in range(numindex + 1):
        row = [None for _ in range(i+1)]
        row[0], row[-1] = 1,1 

        for j in range(1, len(row) -1):
            row[j] = l[i-1][j-1] + l[i-1][j]

        l.append(row)

    return l


pti = pascales_traiangle_index(1)
print(pti)
