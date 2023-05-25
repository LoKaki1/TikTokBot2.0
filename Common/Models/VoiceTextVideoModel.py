from dataclasses import dataclass
from typing import Any

from moviepy.video.VideoClip import TextClip


@dataclass
class VoiceTextVideoModel:
    text_clip: Any
    start_time: float
    end_time: float
