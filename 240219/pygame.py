import pygame
import sys

# 초기화
pygame.init()

# 화면 설정
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("당구 게임")

# 색깔 정의
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# 공 객체 클래스
class Ball(pygame.sprite.Sprite):
    def __init__(self, color, radius, x, y):
        super().__init__()
        self.image = pygame.Surface([radius * 2, radius * 2])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        pygame.draw.circle(self.image, color, (radius, radius), radius)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.radius = radius

    def update(self):
        # 공의 이동 또는 다른 동작 업데이트
        pass

# 공과 hole 객체 생성
ball = Ball(RED, 20, 400, 300)
hole = Ball(WHITE, 40, 400, 100)

# 그룹 생성
all_sprites = pygame.sprite.Group()
all_sprites.add(ball, hole)

# 게임 루프
running = True
while running:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 화면 지우기
    screen.fill(WHITE)
    
    # 모든 스프라이트 업데이트 및 그리기
    all_sprites.update()
    all_sprites.draw(screen)
    
    # 화면 업데이트
    pygame.display.flip()

# 종료
pygame.quit()
sys.exit()
