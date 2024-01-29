import pygame
import sys
import random
import time

pygame.init()

WIDTH, HEIGHT = 400, 600
BIRD_SIZE = 40
PIPE_WIDTH, PIPE_HEIGHT = 70, 400
GRAVITY = 0.1
JUMP_STRENGTH = 2
PIPE_SPEED = 2
PIPE_SPACING = 250
is_paused = False


BACKGROUND_COLOR = (89, 172, 255)
GROUND_COLOR = (240, 230, 140)
WHITE = (255, 255, 255)
GREEN = (34, 139, 34)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dev Duniya Flappy Bird Game")

bird_img = pygame.image.load("bird.png")
bird_img = pygame.transform.scale(bird_img, (BIRD_SIZE, BIRD_SIZE))

pipe_img = pygame.Surface((PIPE_WIDTH, PIPE_HEIGHT))
pipe_img.fill(GREEN)
font = pygame.font.Font(None, 36)

class Bird:
    def __init__(self):
        self.x = 50
        self.y = HEIGHT // 2
        self.velocity = 0
    def jump(self):
        self.velocity = -JUMP_STRENGTH
    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity
    def draw(self):
        screen.blit(bird_img, (self.x, self.y))
class Pipe:
    def __init__(self, x):
        self.x = x
        self.height = random.randint(100, HEIGHT - 200)
        self.passed = False
    def update(self):
        self.x -= PIPE_SPEED
    def draw(self):
        screen.blit(pipe_img, (self.x, 0), (0, 0, PIPE_WIDTH, self.height))
        screen.blit(pipe_img, (self.x, self.height + PIPE_SPACING), (0, 0, PIPE_WIDTH, HEIGHT))


bird = Bird()
pipes = [Pipe(WIDTH + i * WIDTH // 2) for i in range(2)]

clock = pygame.time.Clock()

score = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not is_paused:
                    bird.jump()
            if event.key == pygame.K_p:
                is_paused = not is_paused

    if not is_paused:
        bird.update()
        if pipes[-1].x < WIDTH - WIDTH // 2:
            pipes.append(Pipe(WIDTH))
        if pipes[0].x < -PIPE_WIDTH:
            pipes.pop(0)
        for pipe in pipes:
            if pipe.x < bird.x + BIRD_SIZE and pipe.x + PIPE_WIDTH > bird.x:
                if bird.y < pipe.height or bird.y + BIRD_SIZE > pipe.height + PIPE_SPACING:
                    is_paused = True
                    break
                elif bird.x > pipe.x and bird.x < pipe.x + PIPE_WIDTH and not pipe.passed:
                    pipe.passed = True
                    score += 1

        for pipe in pipes:
            pipe.update()

    screen.fill(BACKGROUND_COLOR)
    for pipe in pipes:
        pipe.draw()
    bird.draw()

    if is_paused or not is_paused:
        pygame.draw.rect(screen, GROUND_COLOR, (0, HEIGHT - 50, WIDTH, 50))
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)
