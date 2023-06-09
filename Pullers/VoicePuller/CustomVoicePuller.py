import json
import os
from typing import List
from Configurations.VoiceConfiguration.VoiceConfiguration import VoiceConfiguration
from Pullers.VoicePuller.IVoicePuller import IVoicePuller
import requests


class CustomVoicePuller(IVoicePuller):

    def __init__(self, config: VoiceConfiguration):
        self.config = config
        self.payload = {
              "text": "string",
              "voice_settings": {
                "stability": 0,
                "similarity_boost": 0
          }
        }

    def _create_voice_file_from_response(self,
                                         text: str,
                                         voice: str,
                                         filepath: str
                                         ):
        self.payload['text'] = text
        result = requests.post(self.config.url,
                               data=json.dumps(self.payload),
                               headers=self.config.headers
                               )

        with open(filepath, "wb") as out:
            out.write(result.content)

        return filepath

    def pull_voice(self, texts: List[str], voice: str, video_name: str = None) -> List[str]:
        video_name = id(texts) if video_name is None else video_name
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
