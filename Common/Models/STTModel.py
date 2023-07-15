from dataclasses import dataclass
from typing import List, Union, Any


@dataclass
class STTModel:
    text: str
    duration: float
    start_time: float
    end_time: float

    def __len__(self):
        return len(self.text)

    def __add__(self, other):
        stt_model = self.clone()
        stt_model.text += other.text
        stt_model.start_time = stt_model.start_time if stt_model.start_time < other.start_time else other.start_time
        stt_model.end_time = stt_model.end_time if stt_model.end_time > other.end_time else other.end_time
        stt_model.duration = stt_model.end_time - stt_model.start_time

        return stt_model


    def clone(self):
        return STTModel(self.text,
                        self.duration,
                        self.start_time,
                        self.end_time)
