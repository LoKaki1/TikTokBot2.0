from typing import List

from Common.Models.VoiceTextVideoModel import VoiceTextVideoModel


class ITextCreatorManager:

    def create_voice(self, path: str) -> List[VoiceTextVideoModel]:
        """
        :param path:
        :return:
        """