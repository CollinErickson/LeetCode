class Solution(object):
    def maxProfit(self, prices):
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


sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]), 5)

print(sol.maxProfit([7,6,4,3,1]), 0)
