import pygame
import random
import sys

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 150


class Dinosaur(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('trex.png')
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = SCREEN_HEIGHT - self.rect.height - 30

        self.velocity = 0
        self.jump_height = 20

    def update(self):
        self.velocity += 1
        self.rect.y += self.velocity
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height - 30:
            self.rect.y = SCREEN_HEIGHT - self.rect.height - 30
            self.velocity = 0

    def jump(self):
        self.velocity = -10


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


def generate_obstacle(obstacles):
    obstacle = Obstacle(speed=4)
    obstacles.add(obstacle)


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("谷歌恐龙快跑")

    all_sprites = pygame.sprite.Group()
    obstacles = pygame.sprite.Group()
    dinosaur = Dinosaur()

    all_sprites.add(dinosaur)

    clock = pygame.time.Clock()
    frame_count = 0

    score = 0
    score_font = pygame.font.Font(None, 36)
    score_text = score_font.render(str(score), True, (0, 0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_UP):
                if pygame.sprite.spritecollide(dinosaur, obstacles, False):
                    dinosaur.jump()

        # add new obstacles
        if frame_count % 60 == 0:
            generate_obstacle(obstacles)

        # update sprites
        all_sprites.update()
        obstacles.update()

        # remove off-screen obstacles
        for obstacle in obstacles:
            if obstacle.rect.x < -obstacle.rect.width:
                obstacles.remove(obstacle)
                score += 1
                score_text = score_font.render(str(score), True, (0, 0, 0))

        # draw sprites
        screen.fill((255, 255, 255))
        all_sprites.draw(screen)
        obstacles.draw(screen)
        screen.blit(score_text, (SCREEN_WIDTH - 50, 10))

        # update and display frame
        pygame.display.update()
        frame_count += 1
        clock.tick(60)


if __name__ == '__main__':
    main()
