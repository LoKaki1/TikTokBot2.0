from typing import List, Tuple

from moviepy.audio.AudioClip import CompositeAudioClip
from moviepy.audio.io.AudioFileClip import AudioFileClip


class IVoiceCreator:

    def create_voice(self,
                     texts: List[str],
                     video_name: str
                     ) -> Tuple[CompositeAudioClip, List[AudioFileClip]]:
        """
        :return:
        """