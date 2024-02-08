from enum import Enum


class EnumDogAnimState(str, Enum):
    IDLE = "IDLE"
    SNEAK = "SNEAK"
    JUMP = "JUMP"
    SHOW_DUCK = "SHOW_DUCK"
