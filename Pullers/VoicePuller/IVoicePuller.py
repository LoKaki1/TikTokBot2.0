from typing import List


class IVoicePuller:

    def pull_voice(self, texts: List[str], voice: str, video_name: str = None) -> List[str]:
        """
        :param video_name:
        :param voice:
        :param texts:
        :return:
        """
