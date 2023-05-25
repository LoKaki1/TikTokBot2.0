from dataclasses import dataclass


@dataclass
class BackgroundModel:
    background_data: object  # works good for changing technology (like moviepy -> ffmpeg)

