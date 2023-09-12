from dataclasses import dataclass

from dataclasses_json import dataclass_json, LetterCase


@dataclass_json(letter_case=LetterCase.PASCAL)
@dataclass
class SttConfiguration:
    whisper_model_folder: str
