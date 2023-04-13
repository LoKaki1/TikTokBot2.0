from typing import List, Union, Tuple

from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.VideoClip import VideoClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip


class IImageVoiceConnector:

    def connect_image_voice(self,
                            submission: str,
                            ) \
            -> Tuple[Union[VideoClip, CompositeVideoClip], float]:
        """
        :return:
        """