# Check the pranthesis is the right structure or not 
# for example {[]} True
# ({0} false 
# [())] false

# {[]})

def valid_pranthesis(s : str):
    opening_pranthesis = ['(', '[', '{']
    closing_peranthesis = [')', ']', '}']
    d = dict(zip(closing_peranthesis, opening_pranthesis))

    if (s[0] in closing_peranthesis or s[-1] in opening_pranthesis):
        return False 
    
    ind = 0
    result = []

    while (ind < len(s)):
        if (s[ind] in opening_pranthesis):
            result.append(s[ind])
        else:
            need = d[s[ind]]
            if len(result) > 0 and result[-1] == need:
                result.pop()

            else:
                return False 

        ind += 1

    if (len(result) == 0):
        return True 

    else:
        return False 


vp = valid_pranthesis("{[(([]))]}")    
print(vp)