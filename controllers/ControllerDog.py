import pygame

from models.Dog import Dog
from models.enums.EnumDogAnimState import EnumDogAnimState
from views.components.ComponentDog import ComponentDog


class ControllerDog:
    def __init__(self, dog: Dog):
        self.dog: Dog = dog
        self.component_dog = ComponentDog()
        self.is_jumping = True

    def set_dog_start(self):
        self.dog.x_position = 0
        self.dog.y_position = 423
        self.dog.under_cover = False
        self.dog.animation_state = EnumDogAnimState.SNEAK

    def sneak(self):
        speed = 3
        if self.dog.x_position < 551:
            self.dog.x_position += speed
            if self.dog.x_position == 201:
                pygame.time.wait(1000)
            elif self.dog.x_position == 549:
                pygame.time.wait(1000)
        else:
            self.dog.animation_state = EnumDogAnimState.JUMP

    def jump(self):
        speed = 10
        if self.dog.y_position > 200 and self.dog.x_position < 710:
            self.dog.y_position -= speed
            self.dog.x_position += speed
        elif self.dog.y_position < 330:
            self.dog.y_position += speed
        else:
            self.dog.under_cover = True
            self.dog.animation_state = EnumDogAnimState.IDLE

    def draw(self, screen):
        if self.dog.animation_state == EnumDogAnimState.SNEAK:
            self.component_dog.draw(screen, self.dog.x_position, self.dog.y_position, 1)
        elif self.dog.animation_state == EnumDogAnimState.JUMP:
            self.component_dog.draw(screen, self.dog.x_position, self.dog.y_position, 2)

    def update(self):
        self.component_dog.update(self.dog.animation_state)
