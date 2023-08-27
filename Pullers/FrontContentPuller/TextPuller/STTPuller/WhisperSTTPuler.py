from typing import List

import torch.cuda

from Common.Factory.STTModelFactory.ISTTModelFactory import ISTTModelFactory
from Common.LoggerCommon.Logger import logger_info_decorator
from Common.Models.STTModel import STTModel
from Common.RegularCommon.RegularCommon import device_avalible
from Pullers.FrontContentPuller.TextPuller.STTPuller.ISTTPuller import ISTTPuller
import whisper


class WhisperSTTPuller(ISTTPuller):
    def __init__(self, stt_model_factory: ISTTModelFactory):
        self.stt_model_factory = stt_model_factory
        self.device = device_avalible()

    @logger_info_decorator
    def pull_text_from_audio(self, path: str) -> List[STTModel]:
        model = whisper.load_model("base", device=self.device)
        result = model.transcribe(path, word_timestamps=True)

        segments = result['segments'][0:len(result['segments'])]
        stt_models = []

        for segment in segments:
            words = segment['words']
            stt_models += self.stt_model_factory.create_models_factory(words)

        return stt_models
