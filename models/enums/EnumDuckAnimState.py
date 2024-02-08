from enum import Enum


class EnumDuckAnimState(str, Enum):
    IDLE = "IDLE"
    FLY_LEFT = "FLY_LEFT"
    FLY_UP = "FLY_UP"
    FLY_RIGHT = "FLY_RIGHT"
    FALL = "FALL"
    HIT = "HIT"
