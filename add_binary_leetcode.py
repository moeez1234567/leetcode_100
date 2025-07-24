# Given two binary strings a and b, return their sum as a binary string 

# for example a = "11", b = "1"
# output = 100 

def binary_add(a : str, b : str):
    a_bin = int(a , 2)
    b_bin = int(b , 2)

    add_val = a_bin + b_bin 

    bin_ab = bin(add_val)


    return bin_ab[2:]


ba = binary_add("10101", "010101")
print(ba)