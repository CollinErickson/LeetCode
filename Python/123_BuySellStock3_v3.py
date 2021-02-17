class Solution:
    def maxProfit(self, prices):
      days = len(prices)
      if days < 2:
        return 0
      #x = [[None, None, None, None, None] for i in range(days)]
      # 0 no actions yet
      # 1 holding a stock
      # 2 bought and sold, can buy
      # 3 holding the second stock
      # 4 all done
      x = [0,prices[days-1],0,prices[days-1],0]
      #y = [0,0,0,0,0]
      for i in range(days-2, -1, -1):
        #print(i)
        #y[4] = 0
        #y[3] = max(x[4] + prices[i], x[3])
        #y[2] = max(x[3] - prices[i], x[2])
        #y[1] = max(x[2] + prices[i], x[1])
        #y[0] = max(x[1] - prices[i], x[0])
        #x = y
        x = [
          max(x[1] - prices[i], x[0]),
          max(x[2] + prices[i], x[1]),
          max(x[3] - prices[i], x[2]),
          max(x[4] + prices[i], x[3]),
          0
        ]
      #print(x)
      return (x[0])

sol = Solution()
print(sol.maxProfit(prices = [3,3,5,0,0,3,1,4]), 6)
print(sol.maxProfit(prices = [1,2,3,4,5]), 4)
print(sol.maxProfit([7,6,4,3,1]), 0)
print(sol.maxProfit([7]), 0)
print(sol.maxProfit(prices = [1,2,3]), 1)
