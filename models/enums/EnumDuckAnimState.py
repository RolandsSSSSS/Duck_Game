from enum import Enum


class EnumDuckAnimState(str, Enum):
    IDLE = "IDLE"
    FLY_LEFT = "FLY_LEFT"
    FLY_RIGHT = "FLY_RIGHT"
    FALL = "FALL"
    HIT = "HIT"
