class Solution:
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost):
          return -1
        if len(gas) == 1:
          return 0
        vals = [0 for i in range(len(gas))]
        vals[0] = gas[0] - cost[0]
        maxval, maxind = vals[0], 0
        for i in range(1, len(gas)):
          vals[i] = vals[i-1] + gas[i] - cost[i]
          if vals[i] < maxval:
            maxval, maxind = vals[i], i
        #print(vals)
        return (maxind + 1) % len(gas)

sol = Solution()
print(sol.canCompleteCircuit(gas = [1,2,3,4,5], cost = [3,4,5,1,2]))
print(sol.canCompleteCircuit(gas = [2,3,4], cost = [3,4,3]))
