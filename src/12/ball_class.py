import pygame
from random import randint
from common import *

class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        # 呼叫父類別的方法
        super().__init__()
        
        # 設定球顏色
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        # 繪製球
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        self.velocity = [randint(4,8),randint(-8,8)] # 隨機移動x、y軸距離
        
        # 儲存Ball物件至self.rect
        self.rect = self.image.get_rect()
        
    # 每一幀更新球的位置
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
          
    # 設定球反彈的速度
    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8,8)