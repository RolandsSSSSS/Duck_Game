import pygame
from pygame.sprite import Sprite

from models.enums.EnumDuckAnimState import EnumDuckAnimState


class ComponentDuck(Sprite):
    def __init__(self):
        super().__init__()
        self.duck_sprites = pygame.image.load('./resources/images/13056.png')
        self.sprite_width = 36
        self.sprite_height = 36
        self.right_sprites_black = self.load_sprites([(109, 5), (147, 5), (184, 5)])
        self.left_sprites_black = [pygame.transform.flip(sprite, True, False) for sprite in self.right_sprites_black]
        self.current_frame_index = 0
        self.animation_speed = 10

    def load_sprites(self, coordinates):
        sprites = []
        color_key = self.duck_sprites.get_at((1, 1))
        for coord in coordinates:
            sprite = self.get_frame(coord[0], coord[1])
            sprite = pygame.transform.scale(sprite, (self.sprite_width * 3, self.sprite_height * 3))
            sprite.set_colorkey(color_key)
            sprites.append(sprite)
        return sprites

    def get_frame(self, x, y):
        return self.duck_sprites.subsurface(pygame.Rect(x, y, self.sprite_width, self.sprite_height))

    def draw(self, screen, x, y, duck_state: EnumDuckAnimState):
        if duck_state == EnumDuckAnimState.FLY_RIGHT:
            screen.blit(self.right_sprites_black[self.current_frame_index], (x, y))
        elif duck_state == EnumDuckAnimState.FLY_LEFT:
            screen.blit(self.left_sprites_black[self.current_frame_index], (x, y))

    def update(self):
        self.animation_speed -= 1
        if self.animation_speed <= 0:
            self.current_frame_index += 1
            self.animation_speed = 10
            if self.current_frame_index >= len(self.right_sprites_black):
                self.current_frame_index = 0
