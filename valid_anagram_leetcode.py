# given 2 strings s and t, return True if the t is anagram of s(means that all the words are appear on the other list at once or same time to the other list) 
# for example s = "race", t = "care"
# output = True (because the all the words in t are appear same time in the s)
# s ="carrot", t = "trafic"
# output =  False  



def valid_anagram(s:str, t:str):
    if len(s) != len(t):
        return False 
    
    sl = [str(i) for i in s]
    tl = [str(i) for i in t]
    
    sll = len(sl)


    i = 0
    while (i < sll):
        for ws in sl:
            for wt in tl:
                if ws == wt:
                    sl.remove(ws)
                    tl.remove(wt)
        i += 1


    if len(sl) > 0 and len(tl) > 0:
        return False 
    else:
        return True


              

   
        
    # if len(sl) > 1:
    #     return False 
    # else:
    #     return True


s = "aabc"
t = "efgh"
va = valid_anagram(s,t)
print(va) 



# another way to do that 
def matching_strings(s:str, t:str):
    sl = list(s)
    tl = list(t)
    if sl.sort() == tl.sort():
        return True 
    else:
        return False






s = "racing"
t = "acingr"
ms = matching_strings(s,t)
print(ms) 




# ANOTHER WAY TO DO THAT 
from collections import Counter

def count_string(s:str, t:str): 
    # ls = [str(i) for i in s]
    # lt = [str(i) for i in t]

    ct = dict(Counter(s))
    cs = dict(Counter(t))

    if ct == cs:
        return True 
    else:
        return False





s = "racing"
t = "acingr"
cs = count_string(s,t)