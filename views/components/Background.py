import os
import pygame
from pygame.sprite import Sprite


class Background(Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.background_sprites = pygame.image.load('./resources/images/62618.png')
        self.image = pygame.transform.scale(self.background_sprites, (screen_width, screen_height))
        self.black_sq = self.load_sprites([(63, 240)], 0)
        self.ducks_shot = self.load_sprites([(95, 241)], 18)
        self.rect = self.image.get_rect()

    def load_sprites(self, coordinates, z):
        back_sprites = []
        for coord in coordinates:
            sprite = self.get_frame(coord[0], coord[1])
            sprite = pygame.transform.scale(sprite, (24 + z, 24))
            back_sprites.append(sprite)
        return back_sprites

    def get_frame(self, x, y):
        return self.background_sprites.subsurface(pygame.Rect(x, y, 8, 8))

    def set_sprite_area(self, x, y, width, height):
        self.image = self.background_sprites.subsurface((x, y, width, height))
        self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))

    def draw(self, screen, bullets, ducks_shot):
        screen.blit(self.image, (0, 0))
        for i in range(ducks_shot):
            x_add = i * 40
            screen.blit(self.ducks_shot[0], (474 + x_add, 626))
        if bullets <= 2:
            screen.blit(self.black_sq[0], (210, 622))
            if bullets <= 1:
                screen.blit(self.black_sq[0], (170, 622))
                if bullets == 0:
                    screen.blit(self.black_sq[0], (130, 622))
