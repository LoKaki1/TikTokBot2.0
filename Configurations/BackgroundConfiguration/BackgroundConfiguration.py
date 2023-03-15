from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, LetterCase, config


@dataclass_json(letter_case=LetterCase.PASCAL)
@dataclass
class BackgroundConfiguration:
    background_type: dict
    background_folder: str
    video_length: int
    word_length: int
    background_format: str
    chopped_video_folder: str
