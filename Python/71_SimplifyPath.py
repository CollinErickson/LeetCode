class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        
        s = path.split("/")
        i = 0
        while True:
            #print(s, len(s), i)
            if s[i] == "." or s[i] == "":
                s = s[0:i] + s[(i+1):len(s)]
            elif s[i] == "..":
                if i==0:
                    s = s[(i+1):len(s)]
                else:
                    s = s[0:(i-1)] + s[(i+1):len(s)]
                    i -= 1
            else:
                i += 1
            if i >= len(s):
                break
        t = "/" + "/".join(s)
        
        return t
    

sol = Solution()
print(sol.simplifyPath("/home/"), "/home")
print(sol.simplifyPath("/../"), "/")
print(sol.simplifyPath("/home//foo/"), "/home/foo")
print(sol.simplifyPath("/a/./b/../../c/"), "/c")
print(sol.simplifyPath("/a/../../b/../c//.//"), "/c")
print(sol.simplifyPath("/a//b////c/d//././/.."), "/a/b/c")
