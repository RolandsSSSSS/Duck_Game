import pygame
from pygame.sprite import Sprite

from models.enums.EnumDuckAnimState import EnumDuckAnimState
from models.enums.EnumDuckType import EnumDuckType


class ComponentDuck(Sprite):
    def __init__(self):
        super().__init__()
        self.duck_sprites = pygame.image.load('./resources/images/13056.png')
        self.sprite_width = 36
        self.sprite_height = 36

        self.right_sprites_black = self.load_sprites([(109, 5), (147, 5), (184, 5)], 1)
        self.left_sprites_black = [pygame.transform.flip(sprite, True, False) for sprite in self.right_sprites_black]
        self.hit_sprites_black = self.load_sprites([(221, 5)], 1)
        self.fall_sprites_black = self.load_sprites([(258, 5), (286, 5), (258, 5)], 2)

        self.right_sprites_red = self.load_sprites([(109, 41), (146, 41), (184, 41)], 1)
        self.left_sprites_red = [pygame.transform.flip(sprite, True, False) for sprite in self.right_sprites_red]
        self.hit_sprites_red = self.load_sprites([(221, 41)], 1)
        self.fall_sprites_red = self.load_sprites([(258, 50), (286, 50), (258, 50)], 2)

        self.right_sprites_blue = self.load_sprites([(106, 90), (144, 90), (181, 90)], 1)
        self.left_sprites_blue = [pygame.transform.flip(sprite, True, False) for sprite in self.right_sprites_blue]
        self.hit_sprites_blue = self.load_sprites([(221, 77)], 1)
        self.fall_sprites_blue = self.load_sprites([(257, 92), (285, 92), (257, 92)], 2)

        self.current_frame_index = 0
        self.animation_speed = 10

    def load_sprites(self, coordinates, z):
        sprites = []
        color_key = self.duck_sprites.get_at((1, 1))
        for coord in coordinates:
            sprite = self.get_frame(coord[0], coord[1], z)
            sprite = pygame.transform.scale(sprite, (self.sprite_width * 3, self.sprite_height * 3))
            sprite.set_colorkey(color_key)
            sprites.append(sprite)
        return sprites

    def get_frame(self, x, y, z):
        if z == 1:
            return self.duck_sprites.subsurface(pygame.Rect(x, y, self.sprite_width, self.sprite_height))
        elif z == 2:
            return self.duck_sprites.subsurface(pygame.Rect(x, y, 30, self.sprite_height))

    def draw(self, screen, x, y, duck_state: EnumDuckAnimState, duck_type: EnumDuckType):
        # print(duck_type, duck_state)
        if duck_state == EnumDuckAnimState.FLY_RIGHT:
            if duck_type == EnumDuckType.BLACK:
                screen.blit(self.right_sprites_black[self.current_frame_index], (x, y))
            elif duck_type == EnumDuckType.RED:
                screen.blit(self.right_sprites_red[self.current_frame_index], (x, y))
            elif duck_type == EnumDuckType.BLUE:
                screen.blit(self.right_sprites_blue[self.current_frame_index], (x, y))
        elif duck_state == EnumDuckAnimState.FLY_LEFT:
            if duck_type == EnumDuckType.BLACK:
                screen.blit(self.left_sprites_black[self.current_frame_index], (x, y))
            elif duck_type == EnumDuckType.RED:
                screen.blit(self.left_sprites_red[self.current_frame_index], (x, y))
            elif duck_type == EnumDuckType.BLUE:
                screen.blit(self.left_sprites_blue[self.current_frame_index], (x, y))
        elif duck_state == EnumDuckAnimState.HIT:
            if duck_type == EnumDuckType.BLACK:
                screen.blit(self.hit_sprites_black[0], (x, y))
            elif duck_type == EnumDuckType.RED:
                screen.blit(self.hit_sprites_red[0], (x, y))
            elif duck_type == EnumDuckType.BLUE:
                screen.blit(self.hit_sprites_blue[0], (x, y))
        elif duck_state == EnumDuckAnimState.FALL:
            if duck_type == EnumDuckType.BLACK:
                screen.blit(self.fall_sprites_black[self.current_frame_index], (x, y))
            elif duck_type == EnumDuckType.RED:
                screen.blit(self.fall_sprites_red[self.current_frame_index], (x, y))
            elif duck_type == EnumDuckType.BLUE:
                screen.blit(self.fall_sprites_blue[self.current_frame_index], (x, y))

    def update(self, duck_state: EnumDuckAnimState):
        self.animation_speed -= 1
        if self.animation_speed <= 0:
            self.current_frame_index += 1
            self.animation_speed = 10
            if duck_state == EnumDuckAnimState.FALL:
                if self.current_frame_index >= len(self.fall_sprites_black):
                    self.current_frame_index = 0
            else:
                if self.current_frame_index >= len(self.right_sprites_black):
                    self.current_frame_index = 0
