import os
from typing import List

import requests

from Common.LoggerCommon.Logger import logger_info_decorator
from Common.VoiceCommon import VoiceCommon
from Configurations.VoiceConfiguration.VoiceConfiguration import VoiceConfiguration
from Pullers.VoicePuller.IVoicePuller import IVoicePuller


class MultipleVoicePuller(IVoicePuller):

    def __init__(self, configuration: VoiceConfiguration):
        self.config = configuration
        self.URI_BASE = self.config.url
        self._session = requests.Session()
        self._session.headers = self.config.headers

    @logger_info_decorator
    def pull_voice(self,
                   texts: List[str],
                   voice: str,
                   video_name: str = None) -> List[str]:
        """
        :param video_name:
        :param voice:
        :param texts:
        :return:
        """
        if video_name is None:
            video_name = id(texts)

        voices_files = self.pull_voices_pair_text(
            texts,
            voice,
            video_name
        )

        return voices_files

    def pull_voices_pair_text(self, texts: List[str], voice: str, video_name: str) -> List[str]:
        voice_path = f"{self.config.output_dir}{video_name}"

        if not os.path.isdir(voice_path):
            os.makedirs(voice_path)

        filepaths = [
            self._create_voice_file_from_response(text,
                                                  voice,
                                                  f'{voice_path}/'
                                                  f'{index}{self.config.file_format}')
            for index, text in enumerate(texts)
        ]

        return filepaths

    def _create_voice_file_from_response(self,
                                         text: str,
                                         voice: str,
                                         filepath: str
                                         ):
        data = self.get_voices(text=text, voice=voice)
        decoded_voices = VoiceCommon.get_audio_from_request(data)

        with open(filepath, "wb") as out:
            out.write(decoded_voices)

        return filepath

    def get_voices(self,
                   text: str,
                   voice: str) -> dict:
        """If voice is not passed, the API will try to use the most fitting voice"""
        voice_request_result = VoiceCommon.create_request(text, voice)
        response = self._session.post(self.URI_BASE, params=voice_request_result)

        return response.json()
