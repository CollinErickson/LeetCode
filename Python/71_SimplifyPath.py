class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        
        return 1
    

sol = Solution()
print(sol.simplifyPath("/home/"), "/home")
print(sol.simplifyPath("/../"), "/")
print(sol.simplifyPath("/home//foo/"), "/home/foo")
print(sol.simplifyPath("/a/./b/../../c/"), "/c")
print(sol.simplifyPath("/a/../../b/../c//.//"), "/c")
print(sol.simplifyPath("/a//b////c/d//././/.."), "/a/b/c")
