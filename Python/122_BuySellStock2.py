class Solution(object):
    def maxProfit(self, prices):
        profit = 0
        x1, x2, x3, p1, p2, p3 = None, None, None, None, None, None
        for i in range(len(prices)):
            if x1 is None:
                #print('c1')
                x1, p1 = i, prices[i]
            elif x2 is None:
                #print('c2')
                x2, p2 = i, prices[i]
                if p2 <= p1:
                    x1, p1, x2, p2 = x2, p2, None, None
            elif x3 is None:
                #print('c3', p2, p3)
                x3, p3 = i, prices[i]
                if p3 >= p2:
                    x2, p2, x3, p3 = x3, p3, None, None
                else:
                    profit += p2 - p1
                    x1, p1, x2, p2, x3, p3 = x3, p3, None, None, None, None
            else:
                print("Fail")
        if p3 is None and p2 is not None:
            profit += p2 - p1
        #elif p3 is None:
        #    print("not possible")
        return profit


sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]), 7)

print(sol.maxProfit([1,2,3,4,5]), 4)

print(sol.maxProfit([7,6,4,3,1]), 0)
print(sol.maxProfit([0]), 0)
print(sol.maxProfit([]), 0)
