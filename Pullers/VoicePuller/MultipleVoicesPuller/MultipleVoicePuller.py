from typing import List

from Pullers.VoicePuller.IVoicePuller import IVoicePuller


class MultipleVoicePuller(IVoicePuller):

    def pull_voice(self, texts: List[str]) -> List[str]:
        """
        :param texts:
        :return:
        """