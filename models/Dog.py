from dataclasses import dataclass

from models.enums.EnumDogAnimState import EnumDogAnimState


@dataclass
class Dog:
    x_position: int = 0
    y_position: int = 0
    under_cover: bool = False
    animation_state: EnumDogAnimState = EnumDogAnimState.IDLE
    animation_duration: float = 0
    animation_start_time: float = 0
    