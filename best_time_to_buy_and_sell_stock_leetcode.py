# given a array of numbers and this is the day in the sequence represent to the stock price in each day you choose the best stock price in the single day
# and sell this in the future and return the maximum profit you can make from this trading 


def buy_sell_stock(prices : list):
    val = prices[0]
    
    ind = 0
    while (ind < len(prices)-1):
        if prices[ind] < val:
            val = prices[ind]
            # print(prices)   
        ind += 1 
    p = prices[prices.index(val):]
    print(p) 

    target = 0
    small = []
    while (target < len(p)):
        if val < p[target]:
            minus = p[target] - val
            small.append(minus) 
        target += 1
            

    if small == []:
        return 0
    
    return max(small)



prices = [10,9,1,8,7]
bss = buy_sell_stock(prices)
print(bss)