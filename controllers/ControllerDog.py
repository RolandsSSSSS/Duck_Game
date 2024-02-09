import pygame

from models.Dog import Dog


class ControllerDog:
    def __init__(self, dog: Dog):
        self.dog: Dog = dog

    def set_animation_duration(self, duration: float):
        pass

    def move_to_start_position(self, screen_height: int):
        self.dog.x_position = 0
        self.dog.y_position = int(screen_height // 1.4)

    def sneak(self, target_x: int):
        speed = 3
        if self.dog.x_position < target_x:
            self.dog.x_position += speed

    def jump(self):
        speed = 5
        if self.dog.y_position > 360 and self.dog.x_position < 710:
            self.dog.y_position -= speed
            self.dog.x_position += speed
        elif self.dog.y_position < 514:
            self.dog.y_position += speed

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.dog.x_position), int(self.dog.y_position)), 50)
