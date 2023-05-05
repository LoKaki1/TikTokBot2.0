from typing import List, Tuple

from Common.Models.STTModel import STTModel


class ISTTPuller:

    def pull_text_from_audio(self, path: str) -> List[STTModel]:
        """
        :param path: path of audio
        :return: text
        """