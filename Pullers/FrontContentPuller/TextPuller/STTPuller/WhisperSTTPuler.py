from typing import List

from Common.Factory.STTModelFactory.ISTTModelFactory import ISTTModelFactory
from Common.LoggerCommon.Logger import logger_info_decorator
from Common.Models.STTModel import STTModel
from Pullers.FrontContentPuller.TextPuller.STTPuller.ISTTPuller import ISTTPuller
import whisper


class WhisperSTTPuller(ISTTPuller):
    def __init__(self, stt_model_factory: ISTTModelFactory):
        self.stt_model_factory = stt_model_factory

    @logger_info_decorator
    def pull_text_from_audio(self, path: str) -> List[STTModel]:
        model = whisper.load_model("base",)
        result = model.transcribe(path, word_timestamps=True)

        segments = result['segments'][0:len(result['segments'])]
        stt_models = []

        for segment in segments:
            words = segment['words']
            stt_models += self.stt_model_factory.create_models_factory(words)

        return stt_models
