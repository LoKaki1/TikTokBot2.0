from dataclasses import dataclass
from typing import List, Union, Any


@dataclass
class STTModel:
    text: str
    time_in_audio: float
