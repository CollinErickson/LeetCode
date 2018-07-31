# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 11:23:52 2018

@author: cbe117
"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dd = {}
        for s in strs:
             t = [let for let in s]
             t.sort()
             u = "".join(t)
             if u in dd:
                 dd[u].append(s)
             else:
                 dd[u] = [s]
        
        return dd.values()
    
sol = Solution()
print sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print [
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]