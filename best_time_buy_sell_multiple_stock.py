# given a prices in a list that prices of stocks of certain days , you need to generate profit from this stock you buy multiple stocks and sale but the 
# rult is that if you buy one stack then you need to sell this and then buy another
# for example prices = [7,1,5,3,6,4] 
# output = 7 (first buy stock at 1 and then sale this in the other day 5 profit is 4 and then again  buy this on 3 and then salwe this in the 6 generate profit from this stock is 3 so total profit is 7) 




def buy_sell_stock(prices):
   total_profit = 0
   sell = []
   i = 1
   while (i < len(prices)):
      if prices[i -1] < prices[i]:
        buy = prices[i-1] 
      
        s = prices[i] - buy 

        sell.append(s)
      
      i += 1 

   for s in sell:
      total_profit += s


   return total_profit


        


prices =[2,4,5,6,7,3,2,1]
bss = buy_sell_stock(prices)
print(bss)