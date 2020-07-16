import numpy as np

width = 3
height = 3
num_states = width * height
S = np.arange(num_states)
A = S.copy()

def showBoard(current_board):
    # p1: x  p2: o
    board = line_to_grid(current_board)
    for i in range(0, 3):
        print('-------------')
        out = '| '
        for j in range(0, 3):
            if board[i, j] == 1:
                token = 'x'
            if board[i, j] == -1:
                token = 'o'
            if board[i, j] == 0:
                token = ' '
            out += token + ' | '
        print(out)
    print('-------------')  #

def reset() -> int:
    return 0

def availablePositions(board) -> list:
    positions = []
    for idx,i in enumerate(board):
        if i == 0:
            positions.append(idx)
    return positions

def is_terminal(current_board) -> (int, bool): #retourne si victoire et qui a gagné
    # lignes

    board = line_to_grid(current_board)

    for i in range(3):
        if sum(board[i, :]) == 3:
            return 1, True
        if sum(board[i, :]) == -3:
            return -1, True
    # colonnes
    for i in range(3):
        if sum(board[:, i]) == 3:
            return 1, True
        if sum(board[:, i]) == -3:
            return -1, True
    # diagonales
    diag_sum1 = sum([board[i, i] for i in range(3)])
    diag_sum2 = sum([board[i, 3 - i - 1] for i in range(3)])
    diag_sum = max(abs(diag_sum1), abs(diag_sum2))
    if diag_sum == 3:
        isEnd = True
        if diag_sum1 == 3 or diag_sum2 == 3:
            return 1, True
        else:
            return -1, True

    # aucune victoire mais partie finie
    if len(availablePositions(current_board)) == 0:
        return 0, True

    # partie en cours
    return None, False

def choose_action(available_positions, current_board, symbol, policy, state,exp_rate=0.3):
    if np.random.uniform(0, 1) <= exp_rate:
        # action random
        idx = np.random.choice(len(available_positions))
        action = available_positions[idx]
    else:
        value_max = -999
        for p in available_positions:
            next_board = current_board.copy()
            next_board[p] = symbol
            if policy[state][p] >= value_max:
                value_max = policy[p][state]
                action = p
    return action

def set_reward(winner,current_board):
    reward = []
    if winner == 0:
        reward = [0 for i in current_board]
    if winner == 1:
        reward = [(10 if i == 1 else (-10 if i == -1 else 0)) for i in current_board]
    if winner == -1:
        reward = [(10 if i == -1 else (-10 if i == 1 else 0)) for i in current_board]

    return reward

def line_to_grid(board):
    return np.array([[board[0],board[1],board[2]], [board[3],board[4],board[5]], [board[6], board[7], board[8]]])

def play_a_game(s0, board, pi, max_steps_per_episode): #lance une partie
    s_list = []
    s_list.append(s0)
    symbol = 1
    isEnd = False
    #showBoard(board)

    while not isEnd:
        # Player 1 ==> IA
        positions = availablePositions(board)
        actual_state = s_list[-1]
        action = choose_action(positions, board, symbol, pi, actual_state)
        # take action and upate board state
        board[action] = symbol
        s_list.append(action)
        symbol = -1
        # check board status if it is end
        #showBoard(board)
        win,isEnd = is_terminal(board)
        if win is not None:
            rewards = set_reward(win,board)
            break

        else:
            # Player 2 ==> random ==> apprentissage fasse au random
            positions = availablePositions(board)
            action = np.random.choice(len(positions))
            board[action] = symbol
            symbol = 1
            #showBoard(board)
            win,isEnd = is_terminal(board)
            if win is not None:
                rewards = set_reward(win,board)
                break


    return s_list,s_list, rewards





