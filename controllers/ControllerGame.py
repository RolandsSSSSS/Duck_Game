import pygame

from models.Duck import Duck
from models.Game import Game
from models.enums.EnumGameState import EnumGameState


class ControllerGame:
    def __init__(self, game: Game, duck: Duck):
        self.game: Game = game
        self.duck: Duck = duck

    def set_game_start(self):
        self.game.state = EnumGameState.RUNNING
        self.game.round_number = 1
        self.game.bullets_left = 3
        self.game.ducks_shot = 0
        self.game.points = 0

    def duck_hit(self):
        self.game.points += self.duck.points
        self.game.bullets_left = 3
        self.game.ducks_shot += 1
        self.next_round()

    def next_round(self):
        if self.game.ducks_shot == 10:
            self.game.round_number += 1
            self.game.ducks_shot = 0
            self.game.points += 1000

    def missed_shot(self):
        self.game.bullets_left -= 1
        if self.game.bullets_left <= 0:
            self.game.state = EnumGameState.GAME_OVER
            with open("points.txt", "w") as file:
                file.write(f"Points: {self.game.points}\n")
                file.write(f"Ducks shot: {self.game.ducks_shot}\n")
            pygame.quit()
