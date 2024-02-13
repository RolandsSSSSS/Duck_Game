import os

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
                file.write(f"Rounds: {self.game.round_number}\n")

            if not os.path.exists("high_score.txt"):
                with open("high_score.txt", "w") as hs_file:
                    hs_file.write("High Score: 0\nRounds: 0\n")

            with open("high_score.txt", "r") as hs_file:
                previous_score = hs_file.read()
                if not previous_score or int(previous_score.split(': ')[1].strip('\nRounds')) < self.game.points:
                    with open("high_score.txt", "w") as hs_file2:
                        hs_file2.write(f"High Score: {self.game.points} \nRounds: {self.game.round_number}\n")
            pygame.quit()
