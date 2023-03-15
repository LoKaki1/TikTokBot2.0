from dataclasses import dataclass
from typing import List, Union, Any


@dataclass
class PullerModel:
    background_puller: str
    front_puller: List[str]
    external_pullers: List[Any]
