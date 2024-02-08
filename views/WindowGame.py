import pygame
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE, MOUSEBUTTONDOWN

from views.components.Background import Background


class WindowGame:
    def __init__(self):
        self.screen_width = 1280
        self.screen_height = 720
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Duck Hunt v0.0.1")
        self.background_sprite = Background(self.screen_width, self.screen_height)

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                elif event.type == MOUSEBUTTONDOWN:
                    pass

            self.background_sprite.set_sprite_area(0, 0, 256, 240)

            self.background_sprite.draw(self.screen)
            pygame.display.flip()
