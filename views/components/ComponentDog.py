import pygame.image
from pygame.sprite import Sprite

from models.enums.EnumDogAnimState import EnumDogAnimState


class ComponentDog(Sprite):
    def __init__(self):
        super().__init__()
        self.dog_sprites = pygame.image.load('./resources/images/62669.png')
        self.sprite_width = 56
        self.sprite_height = 48
        self.sneak_sprites = self.load_sneak_sprites()
        self.jump_sprites = self.load_jump_sprites()
        self.current_frame_index = 0
        self.animation_speed = 10

    def load_sneak_sprites(self):
        sneak_sprites = []
        for x, y in [(0, 9), (56, 9), (112, 9), (168, 9)]:
            sneak_sprite = self.get_frame(x, y, 1)
            sneak_sprite = pygame.transform.scale(sneak_sprite, (self.sprite_width * 3, self.sprite_height * 3))
            sneak_sprite.set_colorkey((99, 173, 255))
            sneak_sprites.append(sneak_sprite)
        return sneak_sprites

    def load_jump_sprites(self):
        jump_sprites = []
        jump_sprite = self.get_frame(0, 185, 2)
        jump_sprite = pygame.transform.scale(jump_sprite, (self.sprite_width * 3, self.sprite_height * 3))
        jump_sprite.set_colorkey((99, 173, 255))
        jump_sprites.append(jump_sprite)
        return jump_sprites

    def get_frame(self, x, y, z):
        if z == 1:
            return self.dog_sprites.subsurface(pygame.Rect(x, y, self.sprite_width, self.sprite_height))
        elif z == 2:
            return self.dog_sprites.subsurface(pygame.Rect(x, y, 40, self.sprite_height))

    def draw(self, screen, x, y, z):
        if z == 1:
            screen.blit(self.sneak_sprites[self.current_frame_index], (x, y))
        elif z == 2:
            screen.blit(self.jump_sprites[0], (x, y))

    def update(self, dog_state: EnumDogAnimState):
        self.animation_speed -= 1
        if dog_state == EnumDogAnimState.JUMP:
            self.current_frame_index = 0
        elif dog_state == EnumDogAnimState.SNEAK:
            if self.animation_speed <= 0:
                self.current_frame_index += 1
                self.animation_speed = 10
                if self.current_frame_index >= len(self.sneak_sprites):
                    self.current_frame_index = 0
