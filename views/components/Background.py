import os
import pygame
from pygame.sprite import Sprite


class Background(Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.background_sprites = pygame.image.load('./resources/images/62618.png')
        self.image = pygame.transform.scale(self.background_sprites, (screen_width, screen_height))
        self.rect = self.image.get_rect()

    def set_sprite_area(self, x, y, width, height):
        self.image = self.background_sprites.subsurface((x, y, width, height))
        self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))

    def draw(self, screen):
        screen.blit(self.image, (0, 0))
