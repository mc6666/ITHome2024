import pygame, sys

# Pygame 初始化
pygame.init()

# 設定各種顏色的RGB
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
RED = (255,0,0)
ORANGE = (255,100,0)
YELLOW = (255,255,0)

score = 0
lives = 3

# 建立視窗
screen = pygame.display.set_mode((800, 600))
# 設定視窗標題
pygame.display.set_caption("打磚塊(Breakout)")

# 控制畫面更新頻率(frame per second, FPS)
clock = pygame.time.Clock()
 
# 監聽鍵盤及滑鼠事件
while True:
    for event in pygame.event.get(): # User did something
        # 關閉視窗，程式即結束
        if event.type == pygame.QUIT: 
              pygame.quit()
              sys.exit()
 
    # 設定視窗背景顏色 
    screen.fill(DARKBLUE)
    # 設定視窗背景顏色 
    pygame.draw.line(screen, WHITE, [0, 38], [800, 38], 2)

    # 建立記分板
    font = pygame.font.Font(None, 34)
    text = font.render("Score: " + str(score), 1, WHITE)
    screen.blit(text, (20,10))
    text = font.render("Lives: " + str(lives), 1, WHITE)
    screen.blit(text, (650,10))
 
    # 更新畫面
    pygame.display.flip()
     
    # 設定每秒60幀(FPS)
    clock.tick(60)
