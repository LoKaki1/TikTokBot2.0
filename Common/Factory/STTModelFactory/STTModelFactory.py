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
