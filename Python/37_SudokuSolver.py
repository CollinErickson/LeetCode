# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 20:36:41 2018

@author: cbe117
"""

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        poss = [[[] for i in range(9)] for j in range(9)]
        # Create poss, possibilities
        for i in range(9):
            for j in range(9):
                #print i,j
                if board[i][j] == ".":
                    poss[i][j] = set([k for k in range(1,10)])
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    # Remove across col
                    for k in [l for l in range(9) if (l!=i and board[l][j]==".")]:
                        #print i,j,k, poss[k][j]
                        poss[k][j] = poss[k][j].difference([int(board[i][j])])
                    # Remove across row
                    for k in [l for l in range(9) if (l!=j and board[i][l]==".")]:
                        poss[i][k] = poss[i][k].difference([int(board[i][j])])
                    # Remove in box
                    igroup = i // 3
                    jgroup = j // 3
                    for k in range(3):
                        for l in range(3):
                            a = igroup*3 + k
                            b = jgroup*3 + l
                            #print i,j,igroup,jgroup,k,l,a,b
                            if not (i==a and j==b) and board[a][b] == ".":
                                poss[a][b] = poss[a][b].difference([int(board[i][j])])
                    #poss[i][j] = set([i for i in range(9)])
        
        # Now begin setting values with only one possibility
        for i in range(1000):
            nochanges = True
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        if len(poss[i][j]) == 1:
                            board[i][j] = str(poss[i][j].pop())
                            poss[i][j] = []
                            self.update_poss(i,j, board, poss)
            if nochanges:
                break
        
        return poss
    def update_poss(self, i, j, board, poss):
        self.pprint(board)
        for k in [l for l in range(9) if (l!=i and board[l][j]==".")]:
            #print i,j,k, poss[k][j]
            poss[k][j] = poss[k][j].difference([int(board[i][j])])
            #if len(poss[k][j]) == 1:
            #    board[k][j] = str(poss[k][j].pop())
            #    poss[k][j] = []
            #    self.update_poss(k, j, board, poss)
            self.check_1poss_and_update(k,j, board, poss)
        # Remove across row
        for k in [l for l in range(9) if (l!=j and board[i][l]==".")]:
            poss[i][k] = poss[i][k].difference([int(board[i][j])])
            #if len(poss[i][k]) == 1:
            #    board[i][k] = str(poss[i][k].pop())
            #    poss[i][k] = []
            #    self.update_poss(i,k, board, poss)
            self.check_1poss_and_update(i,k, board, poss)
        # Remove in box
        igroup = i // 3
        jgroup = j // 3
        for k in range(3):
            for l in range(3):
                a = igroup*3 + k
                b = jgroup*3 + l
                #print i,j,igroup,jgroup,k,l,a,b
                if not (i==a and j==b) and board[a][b] == ".":
                    poss[a][b] = poss[a][b].difference([int(board[i][j])])
                    self.check_1poss_and_update(a,b, board, poss)
        return
    def check_1poss_and_update(self, i, j, board, poss):
        if len(poss[i][j]) == 1:
            board[i][j] = str(poss[i][j].pop())
            poss[i][j] = []
            self.update_poss(i,j, board, poss)
        return
    def pprint(self, board):
        print
        for i in range(9):
            for j in range(9):
                print board[i][j],
            print
        return
    
sol = Solution()
brd = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],
                [".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],
                ["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],
                [".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],
                [".",".",".",".","8",".",".","7","9"]]
po = sol.solveSudoku(brd)
print brd