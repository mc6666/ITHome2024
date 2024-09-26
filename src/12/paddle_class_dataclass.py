import pygame
from dataclasses import dataclass
from common import *

# 反擊板(Paddle)類別 
@dataclass
class Paddle(pygame.sprite.Sprite):
    color:tuple # 顏色
    width:int   # 寬度
    height:int  # 高度
    
    # 設定反擊板影像
    def __post_init__(self):
        # 設定反擊板顏色
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK) # 遇到黑色表透明(transparent)
 
        # 繪製反擊板(Paddle)
        pygame.draw.rect(self.image, self.color, 
            [0, 0, self.width, self.height])
        
        # 儲存Paddle物件至self.rect
        self.rect = self.image.get_rect()
        
    def moveLeft(self, pixels):
        self.rect.x -= pixels
        #Check that you are not going too far (off the screen)
        if self.rect.x < 0:
          self.rect.x = 0
          
    def moveRight(self, pixels):
        self.rect.x += pixels
        #Check that you are not going too far (off the screen)
        if self.rect.x > 700:
          self.rect.x = 700