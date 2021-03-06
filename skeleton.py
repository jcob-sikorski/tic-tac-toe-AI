from pandas import DataFrame
from random import choice


def new_board():
    '''Creates 3x3 board (so-called board) to play with.'''
    board = [['-' for row in range(3)] for rows in range(3)]
    return board


def render(board):
    '''Prints Data Frame of current status of board.'''
    print(DataFrame(board))


def is_invalid_move(board, coordinates):
    '''Checks if the square isn't already taken.'''
    x = coordinates[0]
    y = coordinates[1]
    #print((x, y))

    if board[y][x] != '-':
        return True
    else:
        return False


def empty_squares(board):
    '''Finds every empty square in the given board.'''
    empty_squares = []
    
    for ri, row in enumerate(board):
        for ei, elem in enumerate(row):
            if board[ri][ei] == '-':
                empty_squares.append((ei, ri))
            else:
                pass
    if len(empty_squares) != 0:
        return empty_squares
    else:
        return None


def rotate90Clockwise(board):
    '''Rotates board by 90 degrees clockwise.'''
    board = board
    row = len(board[0]) 
    for i in range(row // 2): 
        for j in range(i, row - i - 1): 
            temp = board[i][j] 
            board[i][j] = board[row - 1 - j][i] 
            board[row - 1 - j][i] = board[row - 1 - i][row - 1 - j] 
            board[row - 1 - i][row - 1 - j] = board[j][row - 1 - i] 
            board[j][row - 1 - i] = temp

    return board


def rotate90AntiClockwise(board):
    '''Rotates matrix by 90 degrees anti clockwise.'''
    N = len(board[0])
    # Consider all squares one by one 
    for x in range(0, int(N/2)): 
          
        # Consider elements in group    
        # of 4 in current square 
        for y in range(x, N-x-1): 
              
            # store current cell in temp variable 
            temp = board[x][y] 
  
            # move values from right to top 
            board[x][y] = board[y][N-1-x] 
  
            # move values from bottom to right 
            board[y][N-1-x] = board[N-1-x][N-1-y] 
  
            # move values from left to bottom 
            board[N-1-x][N-1-y] = board[N-1-y][x] 
  
            # assign temp to left 
            board[N-1-y][x] = temp 

    return board


def random_ai(board):
    '''Randomly chooses not owned square on board.'''
    choosed_square = choice(empty_squares(board))
    return choosed_square

def find_opp_win(board, opponent):
    '''Rudimentary AI choosing last settling move, if such moves aren't possible, chooses randomly.'''
    player = None
    if opponent == 'X':
        player = 'O'
    else:
        player = 'X'
    # checks if settling move haven't been done in horizontal rows
    for ri, row in enumerate(board):
        if row.count(opponent) == 2 and row.count(player) == 0:
            for ei, elem in enumerate(row):
                if board[ri][ei] == '-':
                    return (ei, ri)

    board_length = len(board[0])

    # checks if settling move haven't been done in vertical rows
    for ri, row in enumerate(board):
        if row.count(opponent) == 2 and row.count(player) == 0:
            for ei, elem in enumerate(row):
                if board[ri][ei] == '-':
                    rotate90AntiClockwise(board)
                    if ei == 0 and ri == 0:
                        return (2, 0)
                    else:
                        return (ri, board_length -1 - ei)

    # diagonal from top left to bottom right
    diagonal1 = [board[0][0], board[1][1], board[2][2]]

    if diagonal1.count(opponent) == 2 and diagonal1.count(player) == 0:
        for ei, elem in enumerate(diagonal1):
            if ei == 0 and elem == '-':
                return (0, 0)
            elif ei == 1 and elem == '-':
                return (1, 1)
            elif ei == 2 and elem == '-':
                return (2, 2)

    # diagonal from top right to bottom left
    diagonal2 = [board[0][2], board[1][1], board[2][0]]

    if diagonal2.count(opponent) == 2 and diagonal2.count(player) == 0:
        for ei, elem in enumerate(diagonal2):
            if ei == 0 and elem == '-':
                return (2, 0)
            elif ei == 1 and elem == '-':
                return (1, 1)
            elif ei == 2 and elem == '-':
                return (0, 2)   
    return None 

def finds_winning_move_and_blocks_win_ai(board, player):
    '''Rudimentary AI choosing last settling move, if such moves aren't possible, chooses randomly.'''
    opponent = None
    if player == 'X':
        opponent = 'O'
    else:
        opponent = 'X'
    # checks if settling move haven't been done in horizontal rows
    for ri, row in enumerate(board):
        if row.count(player) == 2 and row.count(opponent) == 0:
            for ei, elem in enumerate(row):
                if board[ri][ei] == '-':

                    return (ei, ri)

    board_length = len(board[0])

    # checks if settling move haven't been done in vertical rows
    for ri, row in enumerate(board):
        if row.count(player) == 2 and row.count(opponent) == 0:

            for ei, elem in enumerate(row):

                if board[ri][ei] == '-':
                    rotate90AntiClockwise(board)
                    if ei == 0 and ri == 0:
                        return (2, 0)
                    else:

                        return (ri, board_length -1 - ei)

    # diagonal from top left to bottom right
    diagonal1 = [board[0][0], board[1][1], board[2][2]]

    if diagonal1.count(player) == 2 and diagonal1.count(opponent) == 0:

        for ei, elem in enumerate(diagonal1):

            if ei == 0 and elem == '-':

                return (0, 0)
            elif ei == 1 and elem == '-':

                return (1, 1)
            elif ei == 2 and elem == '-':

                return (2, 2)

    # diagonal from top right to bottom left
    diagonal2 = [board[0][2], board[1][1], board[2][0]]

    if diagonal2.count(player) == 2 and diagonal2.count(opponent) == 0:

        for ei, elem in enumerate(diagonal2):

            if ei == 0 and elem == '-':

                return (2, 0)
            elif ei == 1 and elem == '-':

                return (1, 1)
            elif ei == 2 and elem == '-':

                return (0, 2)
    # if AI didn't notice any settling move, chooses random move

    if find_opp_win(board, opponent) != None:

        return find_opp_win(board, opponent)
    else:    
        return random_ai(board)

def board_is_full(board):
    '''Checks if the board is filled. Returns True or False.'''
    counter = 0
    # count filled rows
    for i in board:
        if i.count('-') == 0:
            counter += 1
    if counter == 3:
        return True
    else:
        return False

def check_win(board):
    '''Checks if recent move isn't a winning move. If it was returns player. If board is full, returns 'DRAW'. Eventually None.'''
    X = 'X'
    O = 'O'
    count = 0
    # automatically rotates a board to check if settling move wasn't done somewhere in the rows
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

    # diagonal from top left to bottom right
    diagonal1 = [r_board[0][0], r_board[1][1], r_board[2][2]]

    # diagonal from top right to bottom left
    diagonal2 = [r_board[0][2], r_board[1][1], r_board[2][0]]

    # checks if settling move wasn't done in diagonals
    if diagonal1.count(O) == 3 or diagonal2.count(O) == 3:
        return O
    elif diagonal1.count(X) == 3 or diagonal2.count(X) == 3:
        return X
    elif board_is_full(board):
        return 'DRAW'
    else:
        return None

def make_move(board, player):
    '''Puts a pawn on a specific square specified by coordinates.'''

    if player == 'X':
        # HERE YOU CAN CHANGE TYPE OF PLAYER
        coordinates = finds_winning_move_and_blocks_win_ai(board, 'X') 
    else:
        # HERE AN OPPONENT
        coordinates = input('x y: ').split(' ')

    x = int(coordinates[0])
    y = int(coordinates[1])

    if is_invalid_move(board, (x, y)):
        print(f"Can't make move {(x, y)} square is already taken!")
        make_move(board, player)
    else:
        board[y][x] = player
    return board


def game(board, player):
    '''The core of the game.'''

    board = make_move(board, player)
    render(board)

    print('------------')
    if player == 'X':
        player = 'O'
    else:
        player = 'X'

    winner = check_win(board)

    if winner == 'DRAW':
        return 'DRAW'
    elif winner != None:

        print(winner)
        return winner

    board = rotate90Clockwise(rotate90Clockwise(board))

    return game(board, player)

def play_lab(n):
    '''Plays n games and returns statistics about number of wins and draws.'''
    results = []
    for _ in range(n):
        board = new_board()
        #render(board)
        result = game(board, 'X')

        if result == 'X':
            results.append(1)
        elif result == 'O':
            results.append(2)
        else:
            results.append(3)
    stats = {}
    stats['X'] = results.count(1)
    stats['O'] = results.count(2)
    stats['DRAW'] = results.count(3)
    print(f'THE FINAL STATS ARE: {stats}')
    return stats

board = new_board()
render(board)
game(board, 'X')
