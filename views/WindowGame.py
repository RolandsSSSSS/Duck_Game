import pygame
from pygame import QUIT, KEYDOWN, K_ESCAPE


class WindowGame:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Testing pygame")

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

            self.screen.fill((255, 255, 255))
            pygame.draw.circle(self.screen, (0, 0, 255), (400, 300), 75)
            pygame.display.flip()

