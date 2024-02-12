from random import choice, randint

import pygame

from models.Duck import Duck
from models.enums.EnumDuckAnimState import EnumDuckAnimState
from models.enums.EnumDuckType import EnumDuckType
from views.components.ComponentDuck import ComponentDuck


class ControllerDuck:
    def __init__(self, duck: Duck):
        self.duck_hitbox = None
        self.duck: Duck = duck
        self.component_duck = ComponentDuck()

    def set_duck_start(self, screen_width, round_num):
        self.duck.x_position = randint(0, screen_width)
        self.duck.y_position = 350
        self.duck.speed = 4 + 2 * (round_num - 1)
        self.duck.type = choice(list(EnumDuckType))
        self.duck.animation_state = choice([EnumDuckAnimState.FLY_LEFT, EnumDuckAnimState.FLY_RIGHT])
        self.duck.points = 500 + 500 * (round_num - 1)

    def hit(self, mouse_pos):
        if self.duck_hitbox is not None:
            if self.duck_hitbox.collidepoint(mouse_pos):
                self.duck.animation_state = EnumDuckAnimState.HIT

    def start_fall(self):
        self.duck.animation_state = EnumDuckAnimState.FALL

    def fly(self, screen_width):
        if self.duck.animation_state == EnumDuckAnimState.FLY_RIGHT:
            self.duck.x_position += self.duck.speed * 2
            self.duck.y_position -= self.duck.speed // 4
            if self.duck.x_position >= screen_width-108:
                self.duck.animation_state = EnumDuckAnimState.FLY_LEFT
        elif self.duck.animation_state == EnumDuckAnimState.FLY_LEFT:
            self.duck.x_position -= self.duck.speed * 2
            self.duck.y_position -= self.duck.speed // 4
            if self.duck.x_position <= 0:
                self.duck.animation_state = EnumDuckAnimState.FLY_RIGHT
        elif self.duck.animation_state == EnumDuckAnimState.FALL:
            self.duck.y_position += self.duck.speed
        if self.duck.y_position <= -108 or self.duck.y_position >= 350:
            self.duck.animation_state = EnumDuckAnimState.IDLE
        self.duck_hitbox = pygame.Rect(self.duck.x_position, self.duck.y_position, 108, 108)
        # print("Duck hitbox:", self.duck_hitbox)

    def draw(self, screen):
        if self.duck.animation_state != EnumDuckAnimState.IDLE:
            self.component_duck.draw(screen, self.duck.x_position, self.duck.y_position, self.duck.animation_state,
                                     self.duck.type)

    def update(self):
        self.component_duck.update(self.duck.animation_state)
