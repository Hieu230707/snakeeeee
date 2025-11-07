import pygame
from time import sleep
from random import randint

pygame.init() # khỏi động các module để dùng

screen = pygame.display.set_mode((601, 601)) # chiều ngang và chiều dọc của chương trình
pygame.display.set_caption('Snake') # đặt tên chương trình là Snake

# màu RGB
CYAN = (0, 255, 255)
DARK_ORANGE = (255,140,0)
RED = (255, 0, 0)
SKY_BLUE = (135,206,235)
BLACK = (0, 0, 0)

clock = pygame.time.Clock() # giúp giới hạn tốc độ khung hình
running = True


# Tọa độ rắn
snakes = [[5, 10]]
# sang phải -> + 1 tọa độ x
# sang trái -> - 1 tọa độ x
# lên trên -> + 1 tọa độ y
# xuống dưới -> - 1 tọa độ y

direction = 'right' # tự động sang phải khi chạy chương trình

# táo
apple = [randint(0, 19), randint(0, 19)]

#chữ
font_small = pygame.font.SysFont('sans', 20) # chữ cỡ nhỏ để in score
font_big = pygame.font.SysFont('sans', 50) # chữ cỡ lớn để in game over
font_normal = pygame.font.SysFont('sans', 30)
score = 0
pause = False

while running: # cửa số chương trình hiện liên tục
    clock.tick(60) # 60 FPS
    screen.fill(CYAN)

    tail_x = snakes[0][0]
    tail_y = snakes[0][1]
    #DRAW
    for i in range(21):
        pygame.draw.line(screen, SKY_BLUE, (0,i*30), (600, i*30))
        pygame.draw.line(screen, SKY_BLUE, (i*30, 0), (i*30, 600))

    #Draw rắn
    for snake in snakes: # biến snake tạm trong vòng for
        pygame.draw.rect(screen, DARK_ORANGE, (snake[0]*30, snake[1]*30, 30, 30))

    #Draw táo
    pygame.draw.rect(screen, RED, (apple[0]*30, apple[1]*30, 30, 30))

    #Point
    if snakes[-1][0] == apple[0] and snakes[-1][1] == apple[1]:
        snakes.insert(0, [tail_x, tail_y]) # rắn thêm 1 khối ở đầu
        apple = [randint(0, 19), randint(0, 19)]
        score += 1    

    #Score
    score_txt = font_small.render("Score: " + str(score), True, BLACK)
    screen.blit(score_txt, (5, 5))
    #Snake move
    if pause == False:
        if direction == 'right':
            snakes.append([snakes[-1][0]+1, snakes[-1][1]]) # tọa độ x của phần tử cuối cùng +1 và tọa độ y của phần tử cuối cùng
            snakes.pop(0)
        if direction == 'left':
            snakes.append([snakes[-1][0]-1, snakes[-1][1]]) # tọa độ x của phần tử cuối cùng -1 và tọa độ y của phần tử cuối cùng
            snakes.pop(0)
        if direction == 'up':
            snakes.append([snakes[-1][0], snakes[-1][1]-1]) # tọa độ x của phần tử cuối cùng và tọa độ y của phần tử cuối cùng -1
            snakes.pop(0)
        if direction == 'down':
            snakes.append([snakes[-1][0], snakes[-1][1]+1]) # tọa độ x của phần tử cuối cùng và tọa độ y của phần tử cuối cùng +1
            snakes.pop(0)

    #Check đâm vào cạnh
    if snakes[-1][0] < 0 or snakes[-1][0] > 19 or snakes[-1][1] < 0 or snakes[-1][1] > 19:
        pause = True

    #Check cắn đuôi
    for i in range(len(snakes)-1):
        if snakes[-1][0] == snakes[i][0] and snakes[-1][1] == snakes [i][1]:
            pause = True

    #Game over
    if pause == True:
        game_over_txt = font_big.render('GAME OVER', True, BLACK) # render(text: chữ, antialias: (True)làm chữ mượt hơn, color: màu)
        screen.blit(game_over_txt, (190,200)) # in GAME OVER lên màn hình
        score_txt = font_big.render('Score: ' + str(score), True, BLACK)
        screen.blit(score_txt, (225,250))
        press_pause_txt = font_big.render('Press Space to play again', True, BLACK)
        screen.blit(press_pause_txt, (80,300))

    sleep(0.09) # tốc độ /s

    for event in pygame.event.get(): # xét những phím hoặc click chuột
        if event.type == pygame.QUIT: # QUIT là 1 nút của pygame
            running = False
        if event.type == pygame.KEYDOWN: # bấm phím di chuyển
            if event.key == pygame.K_UP and direction != 'down': # bấm lên và hướng khác đi xuống
                direction = 'up'
            if event.key == pygame.K_DOWN and direction != 'up': # bấm xuống và hướng khác đi lên
                direction = 'down'
            if event.key == pygame.K_RIGHT and direction != 'left': # bấm phải và hướng khác sang trái
                direction = 'right'
            if event.key == pygame.K_LEFT and direction != 'right': # bấm trái và hướng khác sang phải
                direction = 'left'
            if event.key == pygame.K_SPACE and pause == True:
                pause = False
                snakes = [[5, 10]]
                apple = [randint(0, 19), randint(0, 19)]
                score = 0
                direction = 'right'

    pygame.display.flip() # cập nhật màu màn hình

pygame.quit() # chạy xong chương trình thì đóng các module của pygame