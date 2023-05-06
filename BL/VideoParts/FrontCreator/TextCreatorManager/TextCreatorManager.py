from typing import List

from moviepy.video.VideoClip import TextClip

from BL.VideoParts.FrontCreator.TextCreator.ITextCreator import ITextCreator
from BL.VideoParts.FrontCreator.TextCreatorManager.ITextCreatorManager import ITextCreatorManager
from Common.Models.VoiceTextVideoModel import VoiceTextVideoModel
from Pullers.FrontContentPuller.TextPuller.STTPuller.ISTTPuller import ISTTPuller


class TextCreatorManager(ITextCreatorManager):

    def __init__(self,
                 text_creator: ITextCreator,
                 stt_puller: ISTTPuller):
        self.stt_puller = stt_puller
        self.text_creator = text_creator

    def create_voice(self, path: str) -> List[VoiceTextVideoModel]:
        stt_models = self.stt_puller.pull_text_from_audio(path)
        text_clips = [VoiceTextVideoModel(self.text_creator.create_text(model.text, model.duration),
                                          model.start_time,
                                          model.end_time,
                                          )

                      for model in stt_models
                      ]

        return text_clips
