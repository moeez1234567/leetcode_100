# given a string s consists of the some words seprated by space return the length of last word of the string if any word cant exists then return the 0 
# for example s = "green lantern"
# output = 7 

# s = " "
# output = 0 

def last_length(string : str):
    if string == "":
        return 0
    

    slt = string.split(" ")
    rslt = slt[-1]

    return len(rslt) 









ll = last_length("")
print(ll)