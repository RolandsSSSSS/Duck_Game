import pygame
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE, MOUSEBUTTONDOWN

from controllers.ControllerDog import ControllerDog
from models.Dog import Dog
from views.components.Background import Background


class WindowGame:
    def __init__(self):
        self.screen_width = 1280
        self.screen_height = 720
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Duck Hunt v0.0.1")
        self.background_sprite = Background(self.screen_width, self.screen_height)
        self.clock = pygame.time.Clock()

        self.dog = Dog()
        self.controller_dog = ControllerDog(self.dog)

    def run(self):
        running = True
        self.controller_dog.move_to_start_position(self.screen_height)

        while running:
            self.clock.tick(60)
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                elif event.type == MOUSEBUTTONDOWN:
                    print("Click")

            print("Dog cords:", self.dog.x_position, self.dog.y_position)

            self.controller_dog.sneak(551)
            if self.dog.x_position > 550:
                self.controller_dog.jump()

            self.background_sprite.set_sprite_area(0, 0, 256, 240)

            self.background_sprite.draw(self.screen)
            self.controller_dog.draw(self.screen)
            pygame.display.flip()
