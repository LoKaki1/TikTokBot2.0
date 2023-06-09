from dataclasses import dataclass

from moviepy.video.VideoClip import TextClip


@dataclass
class VoiceTextVideoModel:
    text_clip: TextClip
    start_time: float
    end_time: float
