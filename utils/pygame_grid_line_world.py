import pygame, sys
import numpy as np

pygame.init()
vec = pygame.math.Vector2
FPS = 60
actions_grid = [[-1,0], [1,0],[0,-1],[0,1]]
actions_line = [[-1,0], [1,0]]


class App():
    def __init__(self,width_screen,height_screen,end_cells,states,plan,type,cell_size,Q,Pi,size,pos,actions):
        self.screen = pygame.display.set_mode((width_screen,height_screen))
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = 'game_screen'
        self.plan = plan
        self.states = states
        self.end_cells = end_cells
        self.type = type
        self.width = width_screen
        self.height = height_screen
        self.cell_size = cell_size
        self.Q = Q
        self.Pi = Pi
        self.size_grid = size
        self.player_pos = pos.copy()
        self.player_begin_pos = pos.copy()
        self.count_move = self.player_begin_pos[0] + self.player_begin_pos[1] * self.size_grid[1]
        self.count_before_move = 0
        self.actions = actions
    def draw_text(self, content, screen, pos, size, colour, font_name, centered=False):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(content, False, colour)
        text_size = text.get_size()
        if centered:
            pos[0] = pos[0] - text_size[0] // 2
            pos[1] = pos[1] - text_size[1] // 2
        screen.blit(text, pos)

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
        self.move_player()

    def draw(self):
        self.screen.fill((0,0,0))
        self.draw_end()
        self.draw_player()
        self.draw_grid()
        pygame.display.update()

    def draw_grid(self):
        for y in range(self.size_grid[1] + 1):
            pygame.draw.line(self.screen, (200, 200, 200), (50, 100 + y * self.cell_size),(self.width - 50, 100 + y * self.cell_size))
        for x in range(self.size_grid[0] + 1):
            pygame.draw.line(self.screen, (200, 200, 200), (50 + x * self.cell_size, 100),(50 + x * self.cell_size, self.height - 100))

        for i in self.end_cells:
            y = i // self.size_grid[0]
            x = i - y * self.size_grid[0]
            self.draw_text("END", self.screen, [65 + x * self.cell_size, 121 + y * self.cell_size], 15,
                           (255, 255, 255), 'arial black')

        for count,i in enumerate(self.Pi):
            direction = 'x'
            value = '0'
            multiple = False
            if np.argmax(i) == 0:
                value = str(np.round(self.Q[count][0], 3))
                direction = '<=='
            elif np.argmax(i) == 1:
                value = str(np.round(self.Q[count][1], 3))
                direction = '==>'
            elif np.argmax(i) == 2:
                value = str(np.round(self.Q[count][2], 3))
                multiple = True
                space = 8
                direction1 = '^'
                direction2 = '||'
            elif np.argmax(i) == 3:
                value = str(np.round(self.Q[count][3], 3))
                multiple = True
                space = 12
                direction1 = '||'
                direction2 = 'v'
            y = count // self.size_grid[0]
            x = count - y * self.size_grid[0]
            if count not in self.end_cells:
                if multiple:
                    self.draw_text(direction1, self.screen, [76 + x * self.cell_size, 126 + y * self.cell_size], 15, (255, 255, 255), 'arial black')
                    self.draw_text(direction2, self.screen, [76 + x * self.cell_size, 126 + space + y * self.cell_size], 15, (255, 255, 255), 'arial black')
                else:
                    self.draw_text(direction, self.screen, [66 + x * self.cell_size, 130 + y * self.cell_size], 15, (255,255,255), 'arial black')

                self.draw_text(value, self.screen, [60 + x * self.cell_size, 105 + y * self.cell_size], 15, (255, 255, 255), 'arial black')

    def draw_end(self):
        for i in self.end_cells:
            if self.plan[0,0,i,1] < 0:
                color = (224,44,44)
            else :
                color = (45,155,238)
            y = i // self.size_grid[0]
            x = i - y * self.size_grid[0]
            pygame.draw.rect(self.screen, color, (51 + x * self.cell_size, 101 + y * self.cell_size, self.cell_size - 1, self.cell_size - 1))

    def draw_player(self):
        pygame.draw.circle(self.screen, (255, 153, 0), (51 + int(self.cell_size / 2) + self.player_pos[0] * self.cell_size,
                                                        101 + int(self.cell_size / 2) + self.player_pos[1] * self.cell_size), int(3 * self.cell_size / 8))

    def move_player(self):

        self.count_before_move += 1
        if self.count_before_move == int(FPS):
            self.count_before_move = 0
            if self.count_move in self.end_cells:
                self.player_pos = self.player_begin_pos.copy()
                self.count_move = self.player_begin_pos[0] + self.player_begin_pos[1] * self.size_grid[1]
            else:
                if (self.type == 'grid'):
                    self.player_pos[0] += actions_grid[self.actions[self.count_move]][0]
                    self.player_pos[1] += actions_grid[self.actions[self.count_move]][1]
                else:
                    self.player_pos[0] += actions_line[self.actions[self.count_move]][0]
                    self.player_pos[1] += actions_line[self.actions[self.count_move]][1]

                if self.actions[self.count_move] == 0:
                    self.count_move -= 1
                elif self.actions[self.count_move] == 1:
                    self.count_move += 1
                elif self.actions[self.count_move] == 2:
                    self.count_move -= self.size_grid[0]
                else:
                    self.count_move += self.size_grid[0]

def display_results(type,Q,Pi,S,T,P,size):
    cell_size = 64
    width = 50 + size[0] * cell_size + 50 #marge gauche + cases longueur grille * taille case + marge droite
    height = 100 + size[1] * cell_size + 100 #marge gauche + cases hauteur grille * taille case + marge droite ==> line world
    if type == 'line':
        begin_pos = [1,0]
    else :
        begin_pos = [0, 0]
    #print(Q)
    #print(Pi)
    #print(S)
    #print(T)
    #print(np.shape(P))
    result = []
    for i in Pi:
        result.append(np.argmax(i))

   # print(result)


    app = App(width,height,T, S, P, type, cell_size, Q, Pi, size, begin_pos, result)
    app.run()