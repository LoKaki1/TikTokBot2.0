from dataclasses import dataclass
from typing import List, Union, Any


@dataclass
class VoiceModel:
    composite: Any  #
    clips: List[Union[str, Any]]  # Any for technology
