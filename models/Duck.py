from dataclasses import dataclass

from models.enums.EnumDuckAnimState import EnumDuckAnimState
from models.enums.EnumDuckType import EnumDuckType


@dataclass
class Duck:
    x_position: int = 0
    y_position: int = 0
    speed: int = 0
    type: EnumDuckType = EnumDuckType.BLACK
    points: int = 0
    animation_state: EnumDuckAnimState = EnumDuckAnimState.IDLE
    animation_duration: float = 0
    animation_start_time: float = 0
