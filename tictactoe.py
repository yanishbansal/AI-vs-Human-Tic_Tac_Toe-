"""
Tic Tac Toe Player
"""
import sys
import math
import copy

X = "X"
O = "O"
EMPTY = None
turn =0

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]



def player(board):
    """
    Returns player who has the next turn on a board.
    """
    isNone=True
    xcount=0
    ocount=0
    for i in range(3):
        for j in range(3):
            if board[i][j]!=None:
                isNone=False
            if board[i][j]==X:
                xcount=1+xcount
            elif board[i][j]==O:
                ocount=ocount+1
    #print(xcount)
    #print(ocount)
    #print(isNone)
    if isNone:
        return X
    else:
        if xcount>ocount:
            return O
        elif ocount==xcount:
            return X
        elif ocount>xcount:
            return X
        
    
        
    
    #raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    List =[]
    for i in range(3):
        for j in range(3):
           if board[i][j]==EMPTY:
               List.append((i,j))
    return List
    #raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    #print(action)
    new_board=copy.deepcopy(board)
    i,j=action
    #print(new_board[i][j])
    if new_board[i][j] is not EMPTY:
        raise Exception ("already have a value in it")
    if player(board)==X:
        new_board[i][j]=X
    else:
        new_board[i][j]=O
    
    return new_board
    #raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range (3):
        if board[i][0]== X and board[i][1] == X and board[i][2] == X :
            return X
        elif board[i][0]==O and board[i][1]==O and board[i][2] ==O:
            return O 
        elif board[0][i] == X and board[1][i] == X and board[2][i] ==X :
            return X
        elif board[0][i]==O and board[1][i]==O and board[2][i] ==O:
            return O 
    
    if board[0][0]== X and board[1][1]== X and board[2][2] ==X:
        return X
    elif board[0][0]==O and board[1][1]==O and board[2][2] ==O:
        return O
    elif board[0][2]== X and board[1][1]== X and board[2][0] ==X:
        return X
    elif board[0][2]==O and board[1][1]==O and board[2][0] ==O:
        return O
    else:
        return None
    
        
    #raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    

    for i in range(3):
        for j in range(3):
            if board[i][j]==EMPTY:
                return False
                
    return True
    #raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board)==X:
            return 1
        elif winner(board)==O:
            return -1
        else:
            return 0
    else:
        raise Exception ("No")
    #raise NotImplementedError

def max_value(board,c):
    if terminal(board):
        return utility(board)
    
    maxi=-3
    available_moves=actions(board)
    for move in available_moves:
        if maxi < min_value(result(board , move),1):
            maxi=min_value(result(board , move),1)
            Move=move
    
    if(c!=0):
        return maxi
    else:
        return Move

    

def min_value(board,c):
    if terminal(board):
        return utility(board)
    
    mini=3
    available_moves=actions(board)
    for move in available_moves:
        if mini > max_value(result(board, move),1):
            mini=max_value(result(board, move),1)
            Move=move
     
    if(c!=0):
        return mini
    else:
        return Move
    

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        Player=player(board)
        if Player ==X:
            return max_value(board,0) #
        elif Player==O:
            return min_value(board,0)

            #min output        
    #raise NotImplementedError

