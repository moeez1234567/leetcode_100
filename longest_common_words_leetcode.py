# Find the Longest Common Words in a String from starting 
# for example strs = ["flight", "flower", "flow"]
# answer = "fl" 

# strs = ["sgd", "gd", "gd"]
# answer = ""

# strs = ["ring","rang", "rung"]

def longest_prefix(strs):
    prefix = ""
    for s in strs:
        if (len(s) < len(prefix) or prefix == ""):
            prefix = s
    
    need = len(strs)
    count = 0 
    result = "" 

    while (need != count):
        count = 0

        for i in strs:
            if (prefix == i[:len(prefix)]):
                count += 1 

        result = prefix
        prefix = prefix[:-1]

        if (need == count):
            return result  
        

lp = longest_prefix(strs = ["ring","rang", "rung"])
print(lp)

     

