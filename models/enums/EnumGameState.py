from enum import Enum


class EnumGameState(str, Enum):
    INITIAL = "INITIAL"
    RUNNING = "RUNNING"
    PAUSED = "PAUSED"
    GAME_OVER = "GAME_OVER"
