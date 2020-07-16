import pygame, sys
import numpy as np
import random

pygame.init()
FPS = 60
screenSize = 500
margin = 50
gameSize = screenSize - (2 * margin)
lineSize = 10

backgroundColor = (0, 0, 0)
lineColor = (255, 255, 255)
xColor = (200, 0, 0)
oColor = (0, 0, 200)

xMark = 'X'
oMark = 'O'


class App():
    def __init__(self, Q, Pi):
        self.screen = pygame.display.set_mode((500, 700))
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = 'game_screen'
        self.board = [[None, None, None], [None, None, None], [None, None, None]]
        self.Q = Q
        self.Pi = Pi
        self.winner = None
        self.IA_wins = 0
        self.random_wins = 0
        self.tie = 0
        self.count_before_move = 0
        self.last_move = None
        self.actual = 0 #à qui le tour? 1 tour du rond, 0 croix

    def get_winner(self):  # retourne si victoire et qui a gagné
        # Diagonals
        if ((self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]) \
            or (self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0])) and self.board[1][1] is not None:
            return self.board[1][1]

        for i in range(3):
            if self.board[i][0] == self.board[i][1] and self.board[i][1] == self.board[i][2] and self.board[i][0] is not None:  # Rows
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] and self.board[1][i] == self.board[2][i] and self.board[0][i] is not None:  # Columns
                return self.board[0][i]

        if len(self.availablePositions()) == 0: #it's a tie
            return 0

        return None #pas fin de partie

    def reset(self):
        self.board = [[None, None, None], [None, None, None], [None, None, None]]
        if self.winner == xMark:
            self.IA_wins += 1
        elif self.winner == oMark:
            self.random_wins += 1
        else:
            self.tie += 1

        self.winner = None

    def draw_lines(self):
        # Vertical lines
        pygame.draw.line(self.screen, lineColor, (margin + gameSize // 3, margin),
                         (margin + gameSize // 3, screenSize - margin), lineSize)
        pygame.draw.line(self.screen, lineColor, (margin + (gameSize // 3) * 2, margin),
                         (margin + (gameSize // 3) * 2, screenSize - margin), lineSize)

        # Horizontal lines
        pygame.draw.line(self.screen, lineColor, (margin, margin + gameSize // 3),
                         (screenSize - margin, margin + gameSize // 3),
                         lineSize)
        pygame.draw.line(self.screen, lineColor, (margin, margin + (gameSize // 3) * 2),
                         (screenSize - margin, margin + (gameSize // 3) * 2), lineSize)

    def draw_board(self):
        myFont = pygame.font.SysFont('Tahoma', gameSize // 3)

        for y in range(3):
            for x in range(3):
                if self.board[y][x] == xMark:
                    color = xColor
                    mark = xMark
                else:
                    mark = oMark
                    color = oColor

                text_surface = myFont.render(self.board[y][x], False, color)
                self.screen.blit(text_surface, (
                y * (gameSize // 3) + margin + (gameSize // 18), x * (gameSize // 3) + margin - (gameSize // 18)))

    def availablePositions(self) -> list:
        positions = []
        for idx, i in enumerate(self.board):
            for idx2,j in enumerate(i):
                if j == None:
                    positions.append([idx,idx2])
        return positions

    def choose_IA(self)->(int,int): ########### PB ICI ############
        available = [i[1] + i[0] * 3 for i in self.availablePositions()]
        print("available moves : ", available)
        if self.last_move != None:
            move = np.argmax([i for idx,i in enumerate(self.Q[self.last_move]) if idx in available])
        else:
            move = np.argmax([i for idx,i in enumerate(self.Q[0]) if idx in available])

        print("Q : ", self.Q[0])
        print("move : ", move)


        return (move//3,move - 3*(move//3))

    def choose_random(self)->(int,int):
        return random.choice(self.availablePositions())

    def run(self):
        while self.running:
            if self.state == 'game_screen':
                self.events()
                self.update()
                self.draw()
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.play()

    def draw(self):
        self.screen.fill(backgroundColor)
        self.draw_board()
        self.draw_lines()
        pygame.display.update()

    def play(self):
        move = [None, None]
        self.count_before_move += 1
        if self.count_before_move == int(FPS):
            print(self.board)
            print(self.availablePositions())

            self.count_before_move = 0
            if self.actual == 0 and self.winner == None:
                move[0],move[1] = self.choose_IA()
                self.board[move[0]][move[1]] = xMark
                print(xMark, move)
                self.actual = 1
            elif self.actual == 1 and self.winner == None:
                move[0],move[1] = self.choose_random()
                self.board[move[0]][move[1]] = oMark
                self.actual = 0
                print(oMark,move)
            print("------------------------------------")
            self.winner = self.get_winner()
            if self.winner != None:

                self.reset()

def display_results(Q,Pi):
    print(Q)
    print(Pi)
    print("-----------------------------")

    app = App(Q,Pi)
    app.run()
