class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        return

sol = Solution()
print(sol.exist([
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
], 'ABCCED'), True)
print(sol.exist([
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
], 'SEE'), True)
print(sol.exist([
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
], 'ABCB'), True)