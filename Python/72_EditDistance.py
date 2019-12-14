class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n = len(word1)
        m = len(word2)
        d = [[0 for i in range(m+1)] for j in range(n+1)]
        
        for i in range(n+1):
            for j in range(m+1):
                if i == 0 and j==0:
                    d[i][j] = 0
                elif i == 0 or j==0:
                    d[i][j] = max(i, j)
                else:
                    if word1[i-1] == word2[j-1]:
                        d[i][j] = d[i-1][j-1]
                    else:
                        d[i][j] = 1 + min(d[i-1][j], d[i][j-1], d[i-1][j-1])
        #print(d)
        return d[n][m]

sol = Solution()
print(sol.minDistance("horse","ros"), 3)
print(sol.minDistance("horse","horse"), 0)
print(sol.minDistance("intention","execution"), 5)