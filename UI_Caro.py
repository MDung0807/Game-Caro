
import pygame
from gameCaro_Algorithm import *


SCREEN_SIZE = (600, 600)
X_O_SIZE = (24, 24)

# Inti the pygame
pygame.init() 

def Init_Game(size):
    matrix = [[0 for i in range(size)]for i in range(size)]
    return matrix

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

    # Init Home
    global home_text, matrix_3x3, matrix_10x10
    home_text = my_font.render('Home', False, (0, 0, 0))
    matrix_3x3 = my_font.render('3x3', False, (0, 0, 0))
    matrix_10x10 = my_font.render('10x10', False, (0, 0, 0))

def Init_Home():
    screen.blit(home_text, (SCREEN_SIZE[0]/2 - home_text.get_width()/2, SCREEN_SIZE[1]/8 - home_text.get_height()))
    global size_3x3, size_10x10
    size_3x3 = screen.blit(matrix_3x3, (SCREEN_SIZE[0]/4 - matrix_3x3.get_width()/2, SCREEN_SIZE[1]/2 - matrix_3x3.get_height()))
    size_10x10 = screen.blit(matrix_10x10, (SCREEN_SIZE[0] * 3/4 - matrix_3x3.get_width()/2, SCREEN_SIZE[1]/2 - matrix_10x10.get_height()))

def End_Game():

    screen.blit(game_over, (SCREEN_SIZE[0]/2 - game_over.get_width()/2, SCREEN_SIZE[1]/2 - game_over.get_height()))
    win = my_font.render(who_win, False, (0, 0, 0))
    screen.blit(win, (SCREEN_SIZE[0]/2 - win.get_width()/2, SCREEN_SIZE[1]/2))
    global restart_game, home_back
    restart_game = screen.blit(restart, (SCREEN_SIZE[0]/2 - restart.get_width()/2, SCREEN_SIZE[1] * 6/8 - restart.get_height()))
    home_back = screen.blit(home_text, (SCREEN_SIZE[0]/2 - home_text.get_width()/2, SCREEN_SIZE[1]* 8/9 - home_text.get_height()))


def Load_UI_Chessboard(N, matrix):
    screen.blit(background, (0, 0))
    for i in range(N):
            for j in range(N):
                # checkerboard print
                box = screen.blit(box_icon, (j*BOX_SIZE[0] + SCREEN_SIZE[0]/2 - BOX_SIZE[0]*N /2, i*BOX_SIZE[1] + SCREEN_SIZE[1]/2 - BOX_SIZE[0]*N /2))
                if matrix[i][j] == 1:
                    screen.blit(x, (j*BOX_SIZE[0] + SCREEN_SIZE[0]/2 - BOX_SIZE[0]*N /2, i*BOX_SIZE[1] + SCREEN_SIZE[1]/2 - BOX_SIZE[0]*N /2))
                elif matrix[i][j] == 2:
                    screen.blit(o, (j*BOX_SIZE[0] + SCREEN_SIZE[0]/2 - BOX_SIZE[0]*N /2, i*BOX_SIZE[1] + SCREEN_SIZE[1]/2 - BOX_SIZE[0]*N /2))

    
def LoopGame():
    global matrix, N

    matrix = None
    N = None

    i_change = None
    j_change = None
    # Win
    global who_win
    who_win = None

    # Game State
    game_state = 'HOME'

    #flag_break
    flag_break = False

    # flag play
    player = True

    # game Loop
    running = True

    while running:
        # RGB: Red, Green, Blue
        screen.fill((0, 0, 0))

        # get mouse location
        mouse_pos = pygame.mouse.get_pos()

        #Background img
        screen.blit(background, (0, 0))

        # Event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Home and Menu
        if game_state == 'HOME':
            Init_Home()
            if event.type == pygame.MOUSEBUTTONUP:
                if size_10x10.collidepoint(mouse_pos):
                    N = 10
                    matrix = Init_Game(N)
                    game_state = 'RUNNING GAME'
                if size_3x3.collidepoint(mouse_pos):
                    N = 3
                    matrix = Init_Game(N)
                    game_state = 'RUNNING GAME'

        if game_state == "RUNNING GAME":
            Load_UI_Chessboard(N, matrix) # Player
            for i in range(N):
                for j in range(N):
                    if matrix[i][j] == 0:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if j*BOX_SIZE[0] + SCREEN_SIZE[0]/2 - BOX_SIZE[0]*N/2 <= mouse_pos[0] and (j+1)*BOX_SIZE[0] + SCREEN_SIZE[0]/2 - BOX_SIZE[0]*N/2 >= mouse_pos[0] and i*BOX_SIZE[0] + SCREEN_SIZE[0]/2 - BOX_SIZE[0]*N/2 <= mouse_pos[1] and (i+1)*BOX_SIZE[0] + SCREEN_SIZE[0]/2 - BOX_SIZE[0]*N/2 >= mouse_pos[1]:
                                matrix[i][j] = 1
                                Load_UI_Chessboard(N, matrix)
                                player = False
                                i_change = i
                                j_change = j
                                if Win(matrix, N, i_change, j_change)[0]:
                                    game_state = 'WAITING'
                                    who_win = 'player win'
                                if IsNodeEnd(matrix, N):
                                    game_state = 'WAITING'
                                flag_break = True
                                break
                if flag_break:
                    flag_break = False
                    break
            
        if game_state == 'WAITING':
            Load_UI_Chessboard(N, matrix)
            screen.blit(title_end_game,(SCREEN_SIZE[0]/2 - title_end_game.get_width()/2, SCREEN_SIZE[1]- title_end_game.get_height()))
            if event.type == pygame.KEYUP:
                game_state = 'END GAME'
                
        
        if game_state == 'END GAME':
            End_Game()
            if event.type == pygame.MOUSEBUTTONUP:
                if restart_game.collidepoint(mouse_pos): 
                    matrix = Init_Game(N)
                    game_state = 'RUNNING GAME'
                    flag_break = False
                    who_win = None
                    i_change = None
                    j_change = None
                    player= True
                if home_back.collidepoint(mouse_pos):
                    game_state = 'HOME'
                    flag_break = False
                    who_win = None
                    i_change = None
                    j_change = None
                    player= True

        pygame.display.update()

        if game_state == 'RUNNING GAME': # AI
            if player == False:
                player = True
                matrix = Run(N, matrix, i_change, j_change)
                if Win(matrix, N, i_change, j_change)[0]:
                    game_state = 'WAITING'
                    who_win = 'AI win'
                if IsNodeEnd(matrix, N):
                    game_state = 'WAITING'
            Load_UI_Chessboard(N, matrix)



    pygame.quit()

if __name__ == '__main__':
    Init_UI()

    LoopGame()

# Bug
"""
- Chưa kiểm tra ô đã đi. (tức là nếu ô đó có giá trị khác 0 thì không được bắt sự kiện) (đã fix)
- Lỗi bên thuật toán: Không tự động kết thúc mặc dù đã thắng (đã fix)
- Lỗi bên AI: Chơi không có mục đích (đã fix)


- Dòng 82 xét thêm trạng thái đang chơi và trạng thái game over (đã fix)
- Kiểm tra xem người chơi thắng hay AI thắng (đã fix)

- THUẬT TOÁN DỪNG Ở CẤP ĐỘ SIZE = 3, CẦN CẢI THIỆN THUẬT TOÁN (đã cải thiện bằng cách tính value)
"""