from typing import Any

from moviepy.video.VideoClip import TextClip


class ITextCreator:

    def create_text(self, text: str, duration: float) -> TextClip:
        """
        :param duration:
        :param text:
        :return:
        """

