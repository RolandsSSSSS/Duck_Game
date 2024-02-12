import pygame
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE, MOUSEBUTTONDOWN

from controllers.ControllerDog import ControllerDog
from controllers.ControllerDuck import ControllerDuck
from controllers.ControllerGame import ControllerGame
from models.Dog import Dog
from models.Duck import Duck
from models.Game import Game
from models.enums.EnumDogAnimState import EnumDogAnimState
from models.enums.EnumDuckAnimState import EnumDuckAnimState
from views.components.Background import Background


class WindowGame:
    def __init__(self):
        self.game = Game()
        self.screen = pygame.display.set_mode((self.game.screen_width, self.game.screen_height))
        pygame.display.set_caption("Duck Hunt v0.0.1")
        self.background_sprite = Background(self.game.screen_width, self.game.screen_height)
        self.clock = pygame.time.Clock()

        self.dog = Dog()
        self.duck = Duck()
        self.controller_dog = ControllerDog(self.dog)
        self.controller_duck = ControllerDuck(self.duck)
        self.controller_game = ControllerGame(self.game, self.duck)

    def run(self):
        running = True
        self.game.round_start = True
        self.controller_dog.set_dog_start()
        self.controller_duck.set_duck_start(self.game.screen_width, self.game.round_number)
        self.controller_game.set_game_start()

        font = pygame.font.SysFont(None, 40)

        while running:
            self.clock.tick(60)
            self.background_sprite.set_sprite_area(0, 0, 256, 240)
            self.background_sprite.draw(self.screen, self.game.bullets_left, self.game.ducks_shot)

            if self.dog.animation_state == EnumDogAnimState.IDLE:
                self.game.round_start = False

            # for now added soo ducks respawns
            if self.duck.animation_state == EnumDuckAnimState.IDLE:
                self.controller_duck.set_duck_start(self.game.screen_width, self.game.round_number)
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                elif event.type == MOUSEBUTTONDOWN:
                    if self.dog.animation_state == EnumDogAnimState.IDLE:
                        mouse_pos = pygame.mouse.get_pos()
                        self.controller_duck.hit(mouse_pos)
                        if self.duck.animation_state == EnumDuckAnimState.HIT:
                            self.controller_game.duck_hit()
                            self.controller_duck.draw(self.screen)
                            self.controller_duck.start_fall()
                        else:
                            self.controller_game.missed_shot()
                        # print("Mouse position:", mouse_pos)

            if self.game.round_start:
                # print("Dog cords:", self.dog.x_position, self.dog.y_position)
                if self.dog.animation_state == EnumDogAnimState.SNEAK:
                    self.controller_dog.sneak()
                elif self.dog.animation_state == EnumDogAnimState.JUMP:
                    self.controller_dog.jump()
                if not self.dog.under_cover:
                    self.controller_dog.draw(self.screen)
                    self.controller_dog.update()
            if not self.game.round_start:
                # print("Duck cords:", self.duck.x_position, self.duck.y_position)
                if self.duck.animation_state != EnumDuckAnimState.IDLE:
                    self.controller_duck.draw(self.screen)
                    self.controller_duck.fly(self.game.screen_width)
                    self.controller_duck.update()

                # for now added so it shows points, bullets, ducks shot on screen
                points = font.render(f"Points: {self.game.points}", True, (255, 255, 255))
                round_number = font.render(f"Round Nr. {self.game.round_number}", True, (255, 255, 255))

                self.screen.blit(points, (10, 10))
                self.screen.blit(round_number, (600, 10))
            pygame.display.flip()
