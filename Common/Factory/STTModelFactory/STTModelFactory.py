from typing import Union

from Common.Factory.STTModelFactory.ISTTModelFactory import ISTTModelFactory
from Common.Models.STTModel import STTModel


class STTModelFactory(ISTTModelFactory):

    def create_model_factory(self, texts: list[str], voices: list) -> list[STTModel]:
        stt_models = []
        start_time = 0

        for voice, text in zip(voices, texts):
            end_time = start_time + voice.duration
            model = STTModel(text, voice.duration, start_time, end_time)

            start_time = end_time
            stt_models.append(model)

        return stt_models

    def create_models_factory(self, tts_models: list[dict[str, Union[str, float]]]) -> list[STTModel]:
        return [
            STTModel(model['word'],
                     (end := model['end']) - (start := model['start']),
                     start,
                     end)
            for model in tts_models
        ]

