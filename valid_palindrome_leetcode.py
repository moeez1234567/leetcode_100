# Given a string s check if its palindrome (means if we reverse this string then it is exact same) of it is same then return True if we reverse this string and its not match then return False 
# and also ignore cases in the string 

# for example input = " a man set on the val"
# output "amansetontheval" return False not palindrome 

# s = "A man, a plan , a canal: Panama"
# output = "amanaplanacanalpanama" return True its plaindrome means if we reverse this sting then it is same exact 

def check_valid_palindrome(s : str):
    lower_s = s.lower() 
    bad_chrs = ",./\''#$%^&*()[]: " ""
    table = str.maketrans("", "", bad_chrs)
    clean_text = lower_s.translate(table) 

    if clean_text == clean_text[::-1]:
        return True 
    else:
        return False



s = "A man, a plan, a canal: Panama"
cvp = check_valid_palindrome(s)
print(cvp) 





# there is a one more way to do this 
def valid_paranthesis(s:str):
    valid = str()
    for v in s:
        if v.isalnum():
            valid += v 
    
    lower_s = valid.lower()

    if lower_s == lower_s[::-1]:
        return True 
    
    else:
        return False 
    


s = "A man, a plan, a canal: Panama"
vp = valid_paranthesis(s)
print(vp)
