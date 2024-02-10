from random import choice, randint

import pygame

from models.Duck import Duck
from models.enums.EnumDuckAnimState import EnumDuckAnimState
from models.enums.EnumDuckType import EnumDuckType
from views.components.ComponentDuck import ComponentDuck


class ControllerDuck:
    def __init__(self, duck: Duck):
        self.duck: Duck = duck
        self.component_duck = ComponentDuck()

    def set_duck_start(self, screen_width):
        self.duck.x_position = randint(0, screen_width)
        self.duck.y_position = 350
        self.duck.speed = 4
        self.duck.duck_type = choice(list(EnumDuckType))
        self.duck.animation_state = choice([EnumDuckAnimState.FLY_LEFT, EnumDuckAnimState.FLY_RIGHT])
        self.duck.points = 500

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
        if self.duck.y_position <= 0:
            self.duck.animation_state = EnumDuckAnimState.IDLE

    def draw(self, screen):
        if self.duck.animation_state != EnumDuckAnimState.IDLE:
            self.component_duck.draw(screen, self.duck.x_position, self.duck.y_position, self.duck.animation_state)

    def update(self):
        self.component_duck.update()
