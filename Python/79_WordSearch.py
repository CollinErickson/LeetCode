import copy
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
                    #print('starting on', i, j, board)
                    if len(word) == 1:
                        return True
                    if self.check4(board, word[1:len(word)], i, j):
                        return True
        
        return False
    def check4(self, board0, word, i, j):
        board = copy.deepcopy(board0) # Need to copy it
        #print('c4', i, j)
        if len(word) == 0:
            return True
        board[i][j] = ''
        #print('did board change?', board0, board)
        if i < len(board)-1:
            if board[i+1][j] == word[0]:
                if len(word) > 1:
                    if self.check4(board, word[1:len(word)], i+1, j):
                        return True
                else:
                    return True
        if i>0:
            if board[i-1][j] == word[0]:
                if len(word) > 1:
                    if self.check4(board, word[1:len(word)], i-1, j):
                        return True
                else:
                    return True
        if j < len(board[0])-1:
            if board[i][j+1] == word[0]:
                if len(word) > 1:
                    if self.check4(board, word[1:len(word)], i, j+1):
                        return True
                else:
                    return True
        if j>0:
            if board[i][j-1] == word[0]:
                if len(word) > 1:
                    if self.check4(board, word[1:len(word)], i, j-1):
                        return True
                else:
                    return True
        return False

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
], 'ABCB'), False)
print(sol.exist([["C","A","A"],["A","A","A"],["B","C","D"]], 
                'AAB'), True)
