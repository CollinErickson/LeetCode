class Solution:
  def maxProfit(self, k, prices):
    if k <= .5 or len(prices) < .5:
      return 0
    # T * (k+1) * 2: T days, 0-k completed buys (must be sold), 0 if not holding 1 if nolding
    x = [[[0, 0] for i in range(0,k+1)] for t in range(len(prices))]
    # On day 0, can buy
    x[0][0][1] = -prices[0]
    for t in range(1, len(prices)):
      # First buy
      # x[t][0][1] = -prices[t]
      for i in range(0, k):
        #print('ti', t, i)
        # State of not owning: can have not owned prev, or just sold
        # if i == 0:
        #   x[t][i][0] = 0
        if i >= 1:
          x[t][i][0] = max(x[t-1][i][0], x[t-1][i-1][1] + prices[t])
        # State of owning: can have prev owned, orjust bought
        # if i == 0:
        #if t==1 and i==0:
        #  print('here:', [x[t-1][i][1], x[t-1][i][0] - prices[t]], '\n\t\t', x)
        x[t][i][1] = max(x[t-1][i][1], x[t-1][i][0] - prices[t])
    #print('x is:', x)
    # Profit is either profit on last day or else add sell on last day
    profit = ([x[len(prices)-1][i][0] for i in range(k+1)])
    return max(profit)

sol = Solution()
# print(sol.maxProfit(k = 2, prices = [2,4,1]), 2)
# print(sol.maxProfit(k = 2, prices = [3,2,6,5,0,3]), 4)
print(sol.maxProfit(1, [2,4,1,0,5,0,7,7,8,9,32,2,4,6,2,4,6,2,4,6,2,2,4,57,7,4,2,1]), 57)
# print(sol.maxProfit(2, [2,4,1,0,5,0,7,7,8,9,32,2,4,6,2,4,6,2,4,6,2,2,4,57,7,4,2,1]), 87)
# # print(sol.maxProfit(5, [2,4,1,0,5,0,7,7,8,9,32,2,4,6,2,4,6,2,4,6,2,2,4,57,7,4,2,1]), 100)
# print(sol.maxProfit(5, [2,4,1,0,5,0,7,7,8,9,32,2,4,6,2,4,6,2,4,6,2,2,4,57,7,4,2,1]), 100)
# print(sol.maxProfit(), )
# print(sol.maxProfit(), )
