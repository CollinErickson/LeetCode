# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 18:36:40 2018

@author: cbe117
"""

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        
        out = [[0 for j in range(n)] for i in range(n)]
        lr = 1
        ud = 0
        r=0
        c=0
        toprowdone = -1
        bottomrowdone = n
        rightcoldone = n
        leftcoldone = -1
        i = 1
        while toprowdone +1 < bottomrowdone and leftcoldone+1 < rightcoldone:
            #print(r,c,out, toprowdone, bottomrowdone, leftcoldone, rightcoldone)
            out[r][c] = i
            if lr == 1:
                if c+1 >= rightcoldone:
                    lr=0
                    ud=1
                    toprowdone += 1
                    r += 1
                else:
                    c += 1
            elif lr == -1:
                if c-1 <= leftcoldone:
                    lr=0
                    ud=-1
                    bottomrowdone -= 1
                    r -= 1
                else:
                    c -= 1
            elif ud == 1:
                if r+1 >= bottomrowdone:
                    lr=-1
                    ud=0
                    rightcoldone -= 1
                    c -= 1
                else:
                    r += 1
            elif ud == -1:
                if r-1 <= toprowdone:
                    lr=1
                    ud=0
                    leftcoldone += 1
                    c += 1
                else:
                    r -= 1
            i += 1
        return out
sol = Solution()
print(sol.generateMatrix(3),'\n',[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
])