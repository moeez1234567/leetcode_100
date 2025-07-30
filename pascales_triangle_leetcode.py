# given a numbers in a row like 1,4,5 and makes a pascales triangle in this rows 
# rules of pascales triangle is that it starts from 1 and the outer side of this triangle is the 1 , and the other values in this list is the increment of the first 2 values 



def pascales_triangle(numrows):
    l = []
    for i in range(numrows):
        row = [None for _ in range(i+1)] 
        row[0], row[-1] = 1,1 

        for j in range(1, len(row)-1):
            row[j] = l[i -1][j - 1] + l[i -1][j]
        l.append(row)

    return l




pt = pascales_triangle(6) # it means triangle have 6 rows
print(pt)