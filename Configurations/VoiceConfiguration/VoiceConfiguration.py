from dataclasses import dataclass
from dataclasses_json import dataclass_json, LetterCase


@dataclass_json(letter_case=LetterCase.PASCAL)
@dataclass
class VoiceConfiguration:
    voice_type: str
    output_dir: str
    file_format: str
    headers: dict
    url: str
