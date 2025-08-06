# given a number integer , return True if this is a happy number and False if this a sad number,  a happy number which at last comes 1 thats the happy number
# for example input = 19
# output = True (happy number because the 1**2 + 9**2 82 bcomes then again 8**2 + 2 **2 64 comes 6**2 + 4**2 it becomes 100 and then 1 comes because 1**2 + 0**2 + 0**2 answer is 1 so happy number 


def happy_number(num : int):
    i = 0
    d = 0
    sums = 0
    st = set()
    # digits = [int(d) for d in str(num)]
    while True:
        digits = [int(d) for d in str(num)]
        for d in digits:
            d = d ** 2 
            sums += d
            # sums = sum(d) 
        num = sums
        sums = 0
        if num in st:
            return False 
        if num == 1:
            return f"Happy Number {True}"
        st.add(num)
        

        


num = 19
h_n = happy_number(num)
print(h_n)
