import numpy as np
def NQueen(board,row):
    if row==len(board):
        display(board)
        return 1
    count=0
    for col in range(len(board)):
        if isSafe(board,row,col):
            board[row][col]=True
            count+=NQueen(board,row+1)
            board[row][col]=False
    return count

def display(board):
    for i in board:
        for j in i:
            if j:
                print("Q",end=" ")
            else:
                print("X",end=" ")
        print("")
    print("")

def isSafe(board,row,col):
    # check vertrical

    for i in range(row):
        if board[i][col]:
            return False
    #check left diagonal
    maxLeft=min(row,col)
    for i in range(1,maxLeft+1):
        if board[row-i][col-i]:
            return False
    #check right diagonal
    maxRight=min(row,len(board)-col-1)
    for i in range(1,maxRight+1):
        if board[row-i,col+i]:
            return False
    return True



# import numpy as np
#
#
# def NQueens(board, r):
#     if (r == len(board)):
#         display(board)
#         return 1
#     count = 0
#     for col in range(len(board)):
#         if isSafe(board, r, col):
#             board[r][col] = True
#             count += NQueens(board, r + 1)
#             board[r][col] = False
#
#     return count
#
#
# def isSafe(board, row, col):
#     for i in range(row):
#         if board[i][col]:
#             return False
#     maxLeft = min(row, col)
#     for i in range(1, maxLeft + 1):
#         if board[row - i][col - i]:
#             return False
#
#     maxRight = min(row, len(board) - col - 1)
#     for i in range(1, maxRight + 1):
#         if board[row - i][col + i]:
#             return False
#     return True
#
#
# def display(board):
#     for i in board:
#         for j in i:
#             if j:
#                 print("Q", end=" ")
#             else:
#                 print("X", end=" ")
#         print("")
#     print('')
#
#
r = 14
c = 14
bool_arr = bool_arr = np.zeros((r, c), dtype=bool)

a = NQueen(bool_arr, 0)
print(a)
