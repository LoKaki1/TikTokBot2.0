from typing import List, Tuple

from moviepy.audio.AudioClip import concatenate_audioclips, CompositeAudioClip
from moviepy.audio.io.AudioFileClip import AudioFileClip

from BL.VideoParts.VoiceCreator.IVoiceCreator import IVoiceCreator
from Common.LoggerCommon.Logger import logger_info_decorator
from Configurations.VoiceConfiguration.VoiceConfiguration import VoiceConfiguration
from Pullers.VoicePuller.IVoicePuller import IVoicePuller


class VoiceCreator(IVoiceCreator):

    def __init__(self,
                 config: VoiceConfiguration,
                 voice_puller: IVoicePuller):
        self.voice_puller = voice_puller
        self.config = config
        self.voice = self.config.voice_type

    @logger_info_decorator
    def create_voice(self,
                     texts: List[str],
                     video_name: str
                     ) -> Tuple[CompositeAudioClip, List[AudioFileClip]]:
        """
        :return:
        """
        audio_files = self.voice_puller.pull_voice(texts, self.voice, video_name)

        audio_clips = [
            AudioFileClip(file)
            for file in audio_files
        ]

        audio_concat = concatenate_audioclips(audio_clips)
        audio_composite = CompositeAudioClip([audio_concat])

        return audio_composite, audio_clips
