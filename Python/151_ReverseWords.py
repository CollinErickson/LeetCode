class Solution:
  def reverseWords(self, s):
    s2 = s.split(" ")
    s3 = [ss for ss in s2 if ss!=""]
    s3.reverse()
    out = " ".join(s3)
    return out

sol = Solution()
print(sol.reverseWords("the sky is blue"), "blue is sky the")
print(sol.reverseWords("  hello world  "), "world hello")
print(sol.reverseWords("a good   example"), "example good a")
print(sol.reverseWords("  Bob    Loves  Alice   "), "Alice Loves Bob")
print(sol.reverseWords("Alice does not even like bob"), "bob like even not does Alice")
