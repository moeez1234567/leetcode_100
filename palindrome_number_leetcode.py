# Return a Plaindrom number if its match by its reverse its Palindrome          #Return True if Palindrome False if Not

# examples
#  num 121 
# output 121 True 

# num 10 
# output = 01 False 
# 
# 
# num -131 
# output = 131- 
   

# number = -1214


# rsn = str(number)
# rn = rsn[::-1]
# rni = int(rn)
# if rni == int(number):
#     print("True") 
# else:
#     print("False") 


def palindrome_number(number):
    if number < 0:
        return "False"

    num_str = str(number)
    rev_str = num_str[::-1]
    rev_int = int(rev_str)
    if rev_int == number:
        return "True"
    else:
        return False 
    

pn = palindrome_number(-252)
print(pn)
    


# Palindrome without using the string



def palindrome_without_string(number):
    if (number < 0 or number % 10 == 0 and number != 0):
        return ("Not Palindrome")
    rev = 0
    while (number > rev):
        last_digit = number % 10
        rev = rev * 10 + last_digit
        number = number // 10
    if (number == rev) or (number == rev // 10):
        return True

pws = palindrome_without_string(1221)
print(pws)