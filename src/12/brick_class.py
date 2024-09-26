import pygame
from common import *

class Brick(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        # 呼叫父類別的方法
        super().__init__()

        # 設定磚塊(Brick)顏色
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # 繪製磚塊(Brick)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # 儲存Brick物件至self.rect
        self.rect = self.image.get_rect()