
import pygame
from gameCaro_Algorithm import *

# Inti the pygame
pygame.init() 
SCREEN_SIZE = (600, 600)
X_O_SIZE = (24, 24)


def init(N):
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

def Load_UI(N, maze):
    for i in range(N):
            for j in range(N):
                # checkerboard print
                box = screen.blit(box_icon, (j*BOX_SIZE[0] + SCREEN_SIZE[0]/2 - BOX_SIZE[0]*N /2, i*BOX_SIZE[1] + SCREEN_SIZE[1]/2 - BOX_SIZE[0]*N /2))
                if maze[i][j] == 1:
                    screen.blit(x, (j*BOX_SIZE[0] + SCREEN_SIZE[0]/2 - BOX_SIZE[0]*N /2, i*BOX_SIZE[1] + SCREEN_SIZE[1]/2 - BOX_SIZE[0]*N /2))
                elif maze[i][j] == 2:
                    screen.blit(o, (j*BOX_SIZE[0] + SCREEN_SIZE[0]/2 - BOX_SIZE[0]*N /2, i*BOX_SIZE[1] + SCREEN_SIZE[1]/2 - BOX_SIZE[0]*N /2))

def LoopGame(N, maze):
    init(N)

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
 
        for i in range(N):
            for j in range(N):
                if maze[i][j] == 0:
                    if event.type == pygame.MOUSEBUTTONUP:
                        if j*BOX_SIZE[0] + SCREEN_SIZE[0]/2 - BOX_SIZE[0]*N/2 <= mouse_pos[0] and (j+1)*BOX_SIZE[0] + SCREEN_SIZE[0]/2 - BOX_SIZE[0]*N/2 >= mouse_pos[0] and i*BOX_SIZE[0] + SCREEN_SIZE[0]/2 - BOX_SIZE[0]*N/2 <= mouse_pos[1] and (i+1)*BOX_SIZE[0] + SCREEN_SIZE[0]/2 - BOX_SIZE[0]*N/2 >= mouse_pos[1]:
                            maze[i][j] = 1
                            # if Win(maze):

                            break
        Load_UI(N, maze)
        pygame.display.update()
        res = 0
        for i in range(size):
            for value in maze[i]:
                if value != 0:
                    res +=1

        if res % 2 != 0:
            maze = Run(size, maze)

    pygame.quit()

if __name__ == '__main__':
    size = 3
   
    maze = [[0 for i in range(size)]for i in range(size)]
    LoopGame(size, maze)




# Bug
"""
- Chưa kiểm tra ô đã đi. (tức là nếu ô đó có giá trị khác 0 thì không được bắt sự kiện) (đã fix)
- Lỗi bên thuật toán: Không tự động kết thúc mặc dù đã thắng
- Lỗi bên AI: Chơi không có mục đích


- Dòng 82 xét thêm trạng thái đang chơi và trạng thái game over
- Kiểm tra xem người chơi thắng hay AI thắng

- THUẬT TOÁN DỪNG Ở CẤP ĐỘ SIZE = 3, CẦN CẢI THIỆN THUẬT TOÁN
"""