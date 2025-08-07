# given 2 strings s and t, check if this are isomorphic ( means that they are change into the another alphabets rules of isomorphic is that both strings length are same,
#  if one chracter change to another chracter then it cant be assign agaian with another chracter , indexing like 0th index chracter only maps with the oth index chracter of anther string)


def isomorphic_strings(s: str, t: str):
    if len(s) != len(t):
        return False

    se = set(s)
    te = set(t)

    if len(se) != len(te):
        return False
    else:
        return True


s = "badc"
t = "baba"
iss = isomorphic_strings(s, t)
print(iss)


# accurate way 
def isomorphic__strings(s,t):
    if len(s) != len(t):
        return False 
    sot = {}
    tos = {}

    for char_s, char_t in zip(s,t):
        if char_s in sot:
            if sot[char_s] != char_t:
                return False 
            
        else:
            sot[char_s] = char_t 

        if char_t in tos:
            if tos[char_t] != char_s:
                return False 
        else:
            tos[char_t] = char_s 


    return True 
            




s = "from"
t = "foor"

i_s = isomorphic__strings(s,t)
print(i_s) 

# s = toip
# t = noop


# another way to do that
def isomorphic(s,t):
    if len(s) != len(t):
        return False 

    mapping = {}

    for i,j in zip(s,t):
        mapping[i] = j 


    if len((set(mapping.values()))) != len(mapping.values()):
        return False  
    
    new_str = ""

    for i in s:
        new_str += mapping[i]

    if new_str != t:
        return False 



    return True 


s = "toip"
t = "noop"
i = isomorphic(s,t)
print(i)

