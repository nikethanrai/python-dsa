import numpy as np


def NKnight(board,r,c,knight):
    if knight==0:
        display(board)
        return
    if r==len(board)-1 and c==len(board):
        return
    if c==len(board):
        NKnight(board,r+1,0,knight)
        return
    if isSafe(board,r,c):
        board[r][c]=True
        NKnight(board,r,c+1,knight-1)
        board[r][c]=False
    NKnight(board,r,c+1,knight)

def isSafe(board,r,c):
    #side left check
    if isValid(board,r-1,c-2):
        if board[r-1][c-2]:
            return False
    #top left check
    if isValid(board,r-2,c-1):
        if board[r-2][c-1]:
            return False
    #side right check
    if isValid(board,r-1,c+2):
        if board[r-1][c+2]:
            return False
    #top rigth check
    if isValid(board,r-1,c+1):
        if board[r-2][c+1]:
            return False
    return True
def isValid(board,row,col):
    if (row >= 0 and row < len(board) and col >= 0 and col < len(board)):
        return True
    return False



def display(board):
    for i in board:
        for j in i:
            if j:
                print("K",end=" ")
            else:
                print("X",end=" ")
        print("")
    print("")
r=3
c=3
bool_arr = np.zeros((r, c), dtype=bool)
arr=[[False,False,False],[False,False,False],[False,False,False],[False,False,False]]

NKnight(bool_arr,0,0,4)