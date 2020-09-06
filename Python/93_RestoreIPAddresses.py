class Solution(object):
    def restoreIpAddresses(self, s, dots=3):
        """
        :type s: str
        :rtype: List[str]
        """
        
        l = []
        if len(s) <= 0:
            return l
        if dots == 0:
            x = int(s)
            if x >= 0 and x <= 255 and str(x) == s:
                return [s]
            return []
        if dots >= 1:
            if len(s) <= dots or len(s) >= 3*(dots+1) + 1:
                return []
            # 1
            l1 = self.restoreIpAddresses(s[1:], dots-1)
            l1 = [s[0] + "." + xx for xx in l1]
            l += l1
            # 2
            if str(int(s[0:2])) == s[0:2]:
                l2 = self.restoreIpAddresses(s[2:], dots-1)
            else:
                l2 = []
            l2 = [s[0:2] + "." + xx for xx in l2]
            l += l2
            # 3
            l3=[]
            if len(s) >= 3 + dots:
                x = int(s[0:3])
                if x >= 0 and x <= 255 and str(x) == s[0:3]:
                    l3 = self.restoreIpAddresses(s[3:], dots-1)
                    l3 = [s[0:3] + "." + xx for xx in l3]
                    l += l3
            #print(l1,l2,l3)
        return l

sol = Solution()

print(sol.restoreIpAddresses("25525511135"), ["255.255.11.135","255.255.111.35"])
print(sol.restoreIpAddresses("12", 0), ["12"])
print(sol.restoreIpAddresses("1233", 0), [])
print(sol.restoreIpAddresses("12", 1), ["1.2"])
print(sol.restoreIpAddresses("123", 1), ["1.23", "12.3"])
print(sol.restoreIpAddresses("1234", 1), ['123.4','12.34','1.234'])
print(sol.restoreIpAddresses("010010"), ["0.10.0.10","0.100.1.0"])

str(int('010')) == "010"
