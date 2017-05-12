# -*- coding: utf-8 -*-
"""
Created on Wed May 10 09:31:01 2017

@author: cbe117
"""

class Solution(object):
    num2chars = {"2":["a","b","c"],
                 "3":["d","e","f"],
                 "4":["g","h","i"],
                 "5":["j","k","l"],
                 "6":["m","n","o"],
                 "7":["p","q","r","s"],
                 "8":["t","u","v"],
                 "9":["w","x","y","z"],
                 }
    num2charscount = {"2":3,
                      "3":3,
                      "4":3,
                      "5":3,
                      "6":3,
                      "7":4,
                      "8":3,
                      "9":4,
                      }
    def convert(self, i):
        
        return
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ld = len(digits)
        if ld==0:
            return []
        charcounts = [self.num2charscount[i] for i in digits]
        charcountscumprod = [1 for i in range(ld+1)]
        charcountscumprod[0] = 1#charcounts[0]
        for i in range(1, ld+1):
            charcountscumprod[i] = charcountscumprod[i-1] * charcounts[i-1]
        #print charcountscumprod
        numcombs = charcountscumprod[-1]
        
        #combs = ["".join([self.num2chars[digits[ii]][j] for (ii, j) in enumerate(self.convert(i))]) for i in range(numcombs)]
        combs = ["".join([self.num2chars[digits[j]][(i/charcountscumprod[j])%charcounts[j]] for j in range(ld)]) for i in range(numcombs)]
        
        return combs
sol = Solution()
print sol.letterCombinations("234")
print sol.letterCombinations("")