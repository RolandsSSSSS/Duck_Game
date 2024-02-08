from dataclasses import dataclass
from typing import List

from models import Duck
from models.enums.EnumGameState import EnumGameState


@dataclass
class Game:
    def __init__(self):
        state: EnumGameState = EnumGameState.INITIAL
        ducks : List[Duck] = []
        round_number: int = 0
        bullets_left: int = 0
        ducks_shot: int = 0
        points: int = 0
