import pygame

pygame.init()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 150
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("谷歌恐龙快跑")
class Dinosaur(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('trex.png')
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = SCREEN_HEIGHT - self.rect.height - 30
        class Dinosaur(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        ...
        self.velocity = 0
        self.jump_height = 20
        
    def jump(self):
        self.velocity = -10

    def update(self):
        self.velocity += 1
        self.rect.y += self.velocity
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height - 30:
            self.rect.y = SCREEN_HEIGHT - self.rect.height - 30
            self.velocity = 0
            class Obstacle(pygame.sprite.Sprite):
    def __init__(self, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('cactus.png')
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = SCREEN_HEIGHT - self.rect.height - 30
        self.speed = speed

    def update(self):
        self.rect.x -= self.speed
        all_sprites = pygame.sprite.Group()
dinosaur = Dinosaur()

obstacles = pygame.sprite.Group()

speed = 4
score = 0

clock = pygame.time.Clock()
frame_count = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_UP):
            if pygame.sprite.spritecollide(dinosaur, obstacles, False):
                dinosaur.jump()

    frame_count += 