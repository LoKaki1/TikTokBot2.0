from typing import List

from moviepy.video.VideoClip import TextClip


class ITextCreatorManager:

    def create_voice(self, path: str) -> List[TextClip]:
        """
        :param path:
        :return:
        """