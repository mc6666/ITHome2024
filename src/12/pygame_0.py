# pip install pygame
import sys, pygame

# Pygame 初始化
pygame.init()

# 建立視窗
screen = pygame.display.set_mode((320, 240))

# 監聽鍵盤及滑鼠事件
while True:
    for event in pygame.event.get():
        # 關閉視窗，程式即結束
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
