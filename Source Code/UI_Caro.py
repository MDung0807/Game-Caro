
from unittest import runner
import pygame
from gameCaro_Algorithm import *


SCREEN_SIZE = (600, 600)
X_O_SIZE = (24, 24)

# Inti the pygame
pygame.init() 

def Init_Game(size):
    maze = [[0 for i in range(size)]for i in range(size)]
    return maze

def Init_UI():
    #Create the screen
    global screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    global BOX_SIZE
    BOX_SIZE = (32, 32)
    
    #Background
    global background
    background = pygame.image.load('./assets/background.jpg')
    background = pygame.transform.scale(background, SCREEN_SIZE)

    #player and AI
    global x, o
    x = pygame.image.load('./assets/x.png')
    x = pygame.transform.scale(x, X_O_SIZE)

    o = pygame.image.load('./assets/o.png')
    o = pygame.transform.scale(o, X_O_SIZE)

    #Box
    global box_icon
    box_icon = pygame.image.load ('./assets/square.png')
    box_icon = pygame.transform.scale(box_icon, BOX_SIZE)

    #sound
    pygame.mixer.music.load('./assets/KinhDi.mp3')
    pygame.mixer.music.play(-1)

    #Set caption and icon
    global icon
    icon = pygame.image.load('./assets/icon.jfif')
    pygame.display.set_icon(icon)
    pygame.display.set_caption('Ca roooo')

    # Game Over
    global game_over, win, my_font
    pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    game_over = my_font.render('Game Over', False, (0, 0, 0))

    # Reset game
    global restart
    restart = my_font.render('Restart Game', False, (0, 0, 0))
   
    # Title End Game
    global title_end_game
    title_end_game = my_font.render('press any key to continue', False, (0, 0, 0))


def End_Game():

    screen.blit(game_over, (SCREEN_SIZE[0]/2 - game_over.get_width()/2, SCREEN_SIZE[1]/2 - game_over.get_height()))
    win = my_font.render(who_win, False, (0, 0, 0))
    screen.blit(win, (SCREEN_SIZE[0]/2 - win.get_width()/2, SCREEN_SIZE[1]/2))
    global restart_game
    restart_game = screen.blit(restart, (SCREEN_SIZE[0]/2 - restart.get_width()/2, SCREEN_SIZE[1]/2 + win.get_height() + game_over.get_height() + 50))

def Load_UI_Chessboard(N, maze):
    
        
    for i in range(N):
            for j in range(N):
                # checkerboard print
                box = screen.blit(box_icon, (j*BOX_SIZE[0] + SCREEN_SIZE[0]/2 - BOX_SIZE[0]*N /2, i*BOX_SIZE[1] + SCREEN_SIZE[1]/2 - BOX_SIZE[0]*N /2))
                if maze[i][j] == 1:
                    screen.blit(x, (j*BOX_SIZE[0] + SCREEN_SIZE[0]/2 - BOX_SIZE[0]*N /2, i*BOX_SIZE[1] + SCREEN_SIZE[1]/2 - BOX_SIZE[0]*N /2))
                elif maze[i][j] == 2:
                    screen.blit(o, (j*BOX_SIZE[0] + SCREEN_SIZE[0]/2 - BOX_SIZE[0]*N /2, i*BOX_SIZE[1] + SCREEN_SIZE[1]/2 - BOX_SIZE[0]*N /2))

    
def LoopGame(N, maze):
    Init_UI()

    # Win
    global who_win
    who_win = None

    # Game State
    game_state = True

    # Wait
    wait = True

    # game Loop
    running = True
    while running:

        # RGB: Red, Green, Blue
        screen.fill((0, 0, 0))

        # get mouse location
        mouse_pos = pygame.mouse.get_pos()

        #Background img
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
            if game_state == False:
                if event.type == pygame.KEYUP or event.type == pygame.MOUSEBUTTONUP:
                    wait = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if wait == False and restart_game.collidepoint(mouse_pos):
                        maze = Init_Game(N)
                        game_state = True
                        wait = True
                        who_win = None
                        
 
        if game_state:
            for i in range(N):
                for j in range(N):
                    if maze[i][j] == 0:
                        if event.type == pygame.MOUSEBUTTONUP:
                            if j*BOX_SIZE[0] + SCREEN_SIZE[0]/2 - BOX_SIZE[0]*N/2 <= mouse_pos[0] and (j+1)*BOX_SIZE[0] + SCREEN_SIZE[0]/2 - BOX_SIZE[0]*N/2 >= mouse_pos[0] and i*BOX_SIZE[0] + SCREEN_SIZE[0]/2 - BOX_SIZE[0]*N/2 <= mouse_pos[1] and (i+1)*BOX_SIZE[0] + SCREEN_SIZE[0]/2 - BOX_SIZE[0]*N/2 >= mouse_pos[1]:
                                maze[i][j] = 1
                                if Win(maze, N):
                                    game_state = False
                                    who_win = 'player win'
                                if IsNodeEnd(maze, N):
                                    game_state = False
                                break
            
        if wait:
            Load_UI_Chessboard(N, maze)
            if game_state == False:
                screen.blit(title_end_game,(SCREEN_SIZE[0]/2 - title_end_game.get_width()/2, SCREEN_SIZE[1]- title_end_game.get_height()))

        elif wait == False:
            End_Game()
            
        if game_state:
            res = 0
            for i in range(N):
                for value in maze[i]:
                    if value != 0:
                        res +=1

            if res % 2 != 0:
                maze = Run(N, maze)
                if Win(maze, N):
                    game_state = False
                    who_win = 'AI win'

        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    size = 3
    maze = Init_Game(size)
    LoopGame(size, maze)

# Bug
"""
- Chưa kiểm tra ô đã đi. (tức là nếu ô đó có giá trị khác 0 thì không được bắt sự kiện) (đã fix)
- Lỗi bên thuật toán: Không tự động kết thúc mặc dù đã thắng (đã fix)
- Lỗi bên AI: Chơi không có mục đích


- Dòng 82 xét thêm trạng thái đang chơi và trạng thái game over (đã fix)
- Kiểm tra xem người chơi thắng hay AI thắng (đã fix)

- THUẬT TOÁN DỪNG Ở CẤP ĐỘ SIZE = 3, CẦN CẢI THIỆN THUẬT TOÁN
"""