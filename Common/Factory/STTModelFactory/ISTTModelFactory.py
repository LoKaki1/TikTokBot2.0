from typing import Union

from Common.Models.STTModel import STTModel


class ISTTModelFactory:

    def create_model_factory(self, texts: list[str], voices: list) -> list[STTModel]:
        """
        :param texts:
        :param voices:
        :return:
        """
    def create_models_factory(self, tts_model: list[dict[str, Union[str, float]]]) -> list[STTModel]:
        """
        :param tts_model:
        :return:
        """