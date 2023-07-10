from Common.Models.STTModel import STTModel


class ISTTModelFactory:

    def create_model_factory(self, texts: list[str], voices: list) -> list[STTModel]:
        """
        :param texts:
        :param voices:
        :return:
        """