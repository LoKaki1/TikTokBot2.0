from typing import List

from Common.Models.STTModel import STTModel
from Pullers.FrontContentPuller.TextPuller.STTPuller.ISTTPuller import ISTTPuller
import whisper


class WhisperSTTPuller(ISTTPuller):

    def pull_text_from_audio(self, path: str) -> List[STTModel]:
        model = whisper.load_model("base", device='cuda')
        result = model.transcribe(path)

        segments = result['segments']
        stt_models = [
            STTModel(segment['text'],
                     (end := segment['end']) - (start := segment['start']),
                     start,
                     end) for segment in segments
        ]

        return stt_models
