class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if len(word) == 1:
                        return True
                    self.check4(board, word[1:len(word)], i, j)
        
        return
    def check4(board, word, i, j):
        
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