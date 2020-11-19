class Solution(object):
    def maxProfit1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        lp = len(prices)
        if lp <= 1:
          return 0
        
        minpricetodate = [prices[0] for i in range(lp)]
        maxpriceafterdate = [prices[lp-1] for i in range(lp)]
        for i in range(1,lp,1):
          minpricetodate[i] = min(minpricetodate[i-1], prices[i])
        for i in range(lp-2,-1,-1):
          maxpriceafterdate[i] = max(maxpriceafterdate[i+1], prices[i])
        diffs = [i-j for i,j in zip(maxpriceafterdate, minpricetodate)]
        #print(minpricetodate, maxpriceafterdate, diffs)
        return max(diffs)
    def maxProfit(self, prices):
        lp = len(prices)
        if lp <= 1:
            return 0
        if lp == 3:
            return self.maxProfit1(prices)
        maxprof = self.maxProfit1(prices)
        for i in range(2, lp - 1):
            iprof = self.maxProfit1(prices[0:i]) + self.maxProfit1(prices[i:lp])
            maxprof = max(maxprof, iprof)
        return maxprof

sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]), 7)

print(sol.maxProfit([1,2,3,4,5]), 4)

print(sol.maxProfit([7,6,4,3,1]), 0)
print(sol.maxProfit([0]), 0)
print(sol.maxProfit([]), 0)

print(sol.maxProfit([3,3,5,0,0,3,1,4]), 6)
print(sol.maxProfit([1,2,3,4,5]), 4)
print(sol.maxProfit([7,6,4,3,1]), 0)

print("Starting slow one...")
print(sol.maxProfit([i for i in range(10000,-1,-1)] + [0 for i in range(1000)]), 0)

