from dataclasses import dataclass
from dataclasses_json import dataclass_json, LetterCase


@dataclass_json(letter_case=LetterCase.PASCAL)
@dataclass
class VideoConnectorConfiguration:
    result_path: str
    tmp_path: str
    width: int
    height: int
    fps: int
    audio_codec: str
    audio_bitrate: str
    fade_in: float
    fade_out: float
    file_format: str
    ffmpeg_files_dir: str
