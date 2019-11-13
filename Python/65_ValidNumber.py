# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 22:35:19 2019

@author: cbe117
"""

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        try:
            float(s)
            return True
        except:
            return False