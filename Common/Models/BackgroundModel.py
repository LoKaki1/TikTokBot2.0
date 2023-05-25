from dataclasses import dataclass
from typing import Any


@dataclass
class BackgroundModel:
    background_data: Any  # works good for changing technology (like moviepy -> ffmpeg)

