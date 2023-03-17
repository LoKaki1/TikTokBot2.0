from typing import List


class IVoicePuller:

    def pull_voice(self, texts: List[str], voice: str) -> List[str]:
        """
        :param voice:
        :param texts:
        :return:
        """
