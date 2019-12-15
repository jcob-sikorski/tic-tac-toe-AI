'''SKELETON FOR TIC TAC TOE AI'''
from pandas import DataFrame

#https://robertheaton.com/2018/10/09/programming-projects-for-advanced-beginners-3-a/

def new_board():
    '''Creates 3x3 matrix (so-called board) to play with.'''
    board = [['-' for row in range(3)] for rows in range(3)]
    return board


def render(board):
    '''Prints Data Frame of current status of board.'''
    print(DataFrame(board))


def is_valid_move(board, coordinates):
    '''Checks if the square isn't already taken.'''
    x = coordinates[0]
    y = coordinates[1]

    if board[y][x] != '-':
        return True
    else:
        return False


def make_move(board, player):
    '''Put a pawn on a specific square specified by coordinates.'''
    print(f'PLAYER: {player}')
    coordinates = input('x y: ').split(' ')
    x = int(coordinates[0])
    y = int(coordinates[1])
    if is_valid_move(board, (x, y)):
        print(f"Can't make move {(x, y)} square is already taken!")
        make_move(board, player)
    else:
        board[y][x] = player
    return board


def rotate90Clockwise(board):
    '''Rotates matrix by 90 degrees clockwise.'''
    row = len(board[0]) 
    for i in range(row // 2): 
        for j in range(i, row - i - 1): 
            temp = board[i][j] 
            board[i][j] = board[row - 1 - j][i] 
            board[row - 1 - j][i] = board[row - 1 - i][row - 1 - j] 
            board[row - 1 - i][row - 1 - j] = board[j][row - 1 - i] 
            board[j][row - 1 - i] = temp

    return board

def board_is_full(board):
    '''Check if the board is filled. Return True or False.'''
    counter = 0
    # count filled rows
    for i in board:
        if i.count('-') == 0:
            counter += 1
    if counter == 3:
        return True
    else:
        return False

def check_winner(board):
    if board_is_full(board):
        print('--DRAW--')
        return 'DRAW'
    else:

        X = 'X'
        O = 'O'
        count = 0
        while count != 2:
            r_board = rotate90Clockwise(board)
            for i in r_board:
                if i.count(O) == 3:
                    return O
                elif i.count(X) == 3:
                    return X
                else:
                    pass
            count += 1

        diagonal1 = [r_board[0][0], r_board[1][1], r_board[2][2]]
        diagonal2 = [r_board[0][2], r_board[1][1], r_board[2][0]]

        # checks if settling move wasn't done in diagonals
        if diagonal1.count(O) == 3 or diagonal2.count(O) == 3:
            return O
        elif diagonal1.count(X) == 3 or diagonal2.count(X) == 3:
            return X
        else:
            return None

        
def update_board():
    '''Update board after new move.'''

def game(board, player):
    board = make_move(board, player)
    render(board)
    print('-----------')
    if player == 'X':
        player = 'O'
    else:
        player = 'X'
    winner = check_winner(board)
    if winner == 'DRAW':
        return None
    elif winner != None:
        print(f'The winner is: {winner}!')
        return winner

    board = rotate90Clockwise(rotate90Clockwise(board))
    return game(board, player)

board = new_board()
render(board)
game(board, 'X')
