from dataclasses import dataclass
from typing import List, Union, Any


@dataclass
class STTModel:
    text: str
    duration: float
    start_time: float
    end_time: float
