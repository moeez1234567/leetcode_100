# given a string like "AB" return their excel sheet number 27 
# input = "AN"
# output = 40 


# input = "ACD"
# output = 758 

def excel_sheet_column(s : str):
    i = 0
    root = 0
    right = len(s) -1 
    l = []
    while (i < len(s)):
        alpha = s[right]
        val = ord(alpha) - 64 
        if len(l) < 1:
            l.append(val)
        else:
            root += 1
            l.append(val * 26 ** root)
        
        i += 1
        right -= 1 


    return sum(l)


s = "ABCD"
esc = excel_sheet_column(s)
print(esc)