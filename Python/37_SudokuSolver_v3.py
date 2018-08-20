# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 09:22:38 2018

@author: cbe117
"""

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
        nochangelastiter = False
        for iteration in range(10):
            #print iteration
            done = True
            nochange = True
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        done = False
                        if len(poss[i][j]) == 1:
                            nochange = False
                            board[i][j] = str(poss[i][j].pop())
                            poss[i][j] = []
                            self.update_poss(i,j, board, poss)
            if done:
                break
            if nochange and nochangelastiter:                
                # Need to check if there are groups where only one value possible
                # Check across rows
                for i in range(9):
                    poss_counts = [0 for iii in range(9)]
                    for j in range(9):
                        for p in poss[i][j]:
                            poss_counts[int(p)-1] += 1
                    #if iteration <= 997 and i ==0:
                    #    print "here", poss_counts
                    #print "poss_counts", i, poss_counts
                    for j in range(9):
                        if poss_counts[j] == 1:
                            for k in range(9):
                                if j+1 in poss[i][k]:
                                    board[i][k] = str(j+1)
                                    poss[i][k] = []
                                    self.update_poss(i,k, board, poss)
                                    nochange = False
                # Check down columns
                for i in range(9):
                    poss_counts = [0 for iii in range(9)]
                    for j in range(9):
                        for p in poss[j][i]:
                            poss_counts[int(p)-1] += 1
                    #if iteration <= 997 and i ==0:
                    #    print "here", poss_counts
                    #print "poss_counts column", i, poss_counts
                    for j in range(9):
                        if poss_counts[j] == 1:
                            for k in range(9):
                                if j+1 in poss[k][i]:
                                    board[k][i] = str(j+1)
                                    poss[k][i] = []
                                    self.update_poss(k,i, board, poss)
                                    nochange = False
                                    #print "THIS_WORKED NOW"
                # NEED in boxes next here
            nochangelastiter = nochange
        else:
            self.solve(board)
        return #poss
    def update_poss(self, i, j, board, poss):
        #self.pprint(board)
        for k in range(9): #[l for l in range(9) if (l!=i and board[l][j]==".")]:
            if k != i and board[k][j]==".":
                #print i,j,k, poss[k][j]
                poss[k][j] = poss[k][j].difference([int(board[i][j])])
                #if len(poss[k][j]) == 1:
                #    board[k][j] = str(poss[k][j].pop())
                #    poss[k][j] = []
                #    self.update_poss(k, j, board, poss)
                self.check_1poss_and_update(k,j, board, poss)
        # Remove across row
        for k in range(9): #[l for l in range(9) if (l!=j and board[i][l]==".")]:
            #print "       ", i, k
            if k!= j and board[i][k] == ".":
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
    
    def solve(self, board):
        i,j = self.findMissing(board)
        if i==-1 and j==-1:
            return True
        #Have indices
        for k in range(1,10):
            #print i,j,k
            if self.isValid(i, j, k, board):
                board[i][j] = str(k)
                if self.solve(board):
                    return True
                # Didn't work
                board[i][j] = "."
        return False
    def findMissing(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    return i,j
        return -1,-1
    def isValid(self, i,j,k,board):
        for a in range(9):
            if a != j and board[i][a] == str(k):
                return False
            if a != i and board[a][j] == str(k):
                return False
        for a in range((i//3)*3, (i//3)*3+3):
            for b in range((j//3)*3, (j//3)*3+3):
                if not (a==i and b==j) and board[a][b] == str(k):
                    return False
        return True
    

if True:   
    sol = Solution()
    brd = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],
                    [".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],
                    ["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],
                    [".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],
                    [".",".",".",".","8",".",".","7","9"]]
    po = sol.solveSudoku(brd)
    pprint(brd)

sol = Solution()
brd2 = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],
        [".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],
        [".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],
        [".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],
        [".",".",".","2","7","5","9",".","."]]
po2 = sol.solveSudoku(brd2)
#for b in brd2: print b #print brd2
sol.pprint(brd2)
