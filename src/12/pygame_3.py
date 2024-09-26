import pygame, sys
from common import *
from paddle_class import Paddle
from ball_class import Ball
from brick_class import Brick

# Pygame 初始化
pygame.init()

score = 0
lives = 3

# 建立視窗
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# 設定視窗標題
pygame.display.set_caption("打磚塊(Breakout)")

# 創建動畫(sprite)群組
all_sprites_list = pygame.sprite.Group()

# 加入反擊板
paddle = Paddle(WHITE, 100, 10)
paddle.rect.x = 350
paddle.rect.y = 560

# 創建 Paddle 物件
paddle = Paddle(LIGHTBLUE, 100, 10)
paddle.rect.x = 350
paddle.rect.y = 560

# 創建 Ball 物件
ball = Ball(WHITE,10,10)
ball.rect.x = 345
ball.rect.y = 195

# 創建三排 Brick 物件
all_bricks = pygame.sprite.Group()
for i in range(7):
    brick = Brick(RED,80,30)
    brick.rect.x = 60 + i* 100
    brick.rect.y = 60
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(7):
    brick = Brick(ORANGE,80,30)
    brick.rect.x = 60 + i* 100
    brick.rect.y = 100
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(7):
    brick = Brick(YELLOW,80,30)
    brick.rect.x = 60 + i* 100
    brick.rect.y = 140
    all_sprites_list.add(brick)
    all_bricks.add(brick)

# 將物件加入動畫(sprite)群組
all_sprites_list.add(paddle)
all_sprites_list.add(ball)

# 控制畫面更新頻率(frame per second, FPS)
clock = pygame.time.Clock()

# 監聽鍵盤及滑鼠事件
carryOn = True
while carryOn:
    for event in pygame.event.get(): # User did something
        # 關閉視窗，程式即結束
        if event.type == pygame.QUIT: 
            #Stop the Game
            carryOn=False
              
    # 控制反擊板水平移動
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        paddle.moveRight(5) 

    # 更新動畫元件 
    all_sprites_list.update()
    
    # 球(Ball)撞到牆會反彈
    if ball.rect.x>=SCREEN_WIDTH-1:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>SCREEN_HEIGHT-1:
        # 球(Ball)掉到螢幕下方，壽命減一
        ball.velocity[1] = -ball.velocity[1]
        lives -= 1
        if lives == 0: # 壽命為0，Game Over
            #Display Game Over Message for 3 seconds
            font = pygame.font.Font(None, 74)
            text = font.render("GAME OVER", 1, WHITE)
            screen.blit(text, (250,300))
            pygame.display.flip()
            pygame.time.wait(3000)

            #Stop the Game
            carryOn=False
    # 球(Ball)碰到螢幕上方會反彈，速度會改變
    if ball.rect.y<40:
        ball.velocity[1] = -ball.velocity[1]

    # 偵測球(Ball)與反擊板(Paddle)碰撞
    if pygame.sprite.collide_mask(ball, paddle):
      ball.rect.x -= ball.velocity[0]
      ball.rect.y -= ball.velocity[1]
      ball.bounce()

    # 避免球(Ball)水平移動
    if ball.velocity[1] == 0:
        ball.velocity[1] = 10

    # 偵測球(Ball)與磚塊(Brick)碰撞
    brick_collision_list = pygame.sprite.spritecollide(ball,all_bricks,False)
    for brick in brick_collision_list:
      ball.bounce()
      score += 1
      brick.kill()
      if len(all_bricks)==0:
           #Display Level Complete Message for 3 seconds
            font = pygame.font.Font(None, 74)
            text = font.render("LEVEL COMPLETE", 1, WHITE)
            screen.blit(text, (200,300))
            pygame.display.flip()
            pygame.time.wait(3000)
            #Stop the Game
            carryOn=False
 
    # 設定視窗背景顏色 
    screen.fill(DARKBLUE)

    # 建立記分板
    pygame.draw.line(screen, WHITE, [0, 38], [800, 38], 2)
    font = pygame.font.Font(None, 34)
    text = font.render("Score: " + str(score), 1, WHITE)
    screen.blit(text, (20,10))
    text = font.render("Lives: " + str(lives), 1, WHITE)
    screen.blit(text, (650,10))
 
    # 更新畫面
    all_sprites_list.draw(screen)
    pygame.display.flip()
     
    # 設定每秒60幀(FPS)
    clock.tick(60)
    
pygame.quit()
