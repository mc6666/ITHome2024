import pygame
from common import *

# 反擊板(Paddle)類別 
class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height): # 顏色、寬度、高度
        # 呼叫父類別的方法
        super().__init__()
        
        # 設定反擊板顏色
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK) # 遇到黑色表透明(transparent)
 
        # 繪製反擊板(Paddle)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        # 儲存Paddle物件至self.rect
        self.rect = self.image.get_rect()
    
    # 向左移動
    def moveLeft(self, pixels):
        self.rect.x -= pixels
        if self.rect.x < 0:
          self.rect.x = 0
          
    # 向右移動
    def moveRight(self, pixels):
        self.rect.x += pixels
        if self.rect.x >= SCREEN_WIDTH-self.rect.width:
          self.rect.x = SCREEN_WIDTH-self.rect.width-1