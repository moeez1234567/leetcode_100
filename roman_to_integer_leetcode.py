# Convert a Roman Numbers into the Integers
def roman_to_int(s : str):
    translation = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }

    s = s.replace("IV", "IIII")
    s = s.replace("IX" , "VIIII")
    s = s.replace("XL" , "XXXX")
    s = s.replace("XC", "LXXXX")
    s = s.replace("CD", "CCCC")
    s = s.replace("CM" , "DCCCC")



    number = 0 
    for r in s:
        number += translation[r]
    return number 
    
rtn = roman_to_int(str(input("Enter Your Roman You want to Convert into Number : ").upper()))
print(rtn)