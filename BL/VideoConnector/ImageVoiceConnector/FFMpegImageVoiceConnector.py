from typing import Tuple, Union, Any

from BL.VideoConnector.ImageVoiceConnector.IImageVoiceConnector import IImageVoiceConnector
from BL.VideoParts.FrontCreator.ImageTextCreator.IImageTextCreator import IImageTextCreator
from BL.VideoParts.VoiceCreator.IVoiceCreator import IVoiceCreator
from Configurations.VideoConnectorConfiguration.VideoConnectorConfiguration import VideoConnectorConfiguration
from Pullers.VoicePuller.IVoicePuller import IVoicePuller


class FFMpegImageVoiceCreator(IImageVoiceConnector):

    def __init__(self,
                 config: VideoConnectorConfiguration,
                 image_creator: IImageTextCreator,
                 voice_creator: IVoiceCreator
                 ):
        self.image_creator = image_creator
        self.voice_creator = voice_creator
        self.config = config

    def connect_image_voice(self,
                            submission: str,
                            ffmpeg_base_video=None
                            ) -> Tuple[Any, float]:
        if ffmpeg_base_video is None:
            raise Exception("ffmpeg base can't be none")

        images = self.image_creator.create_image_text(submission)
        texts = [text.text for text in images]
        voice = self.voice_creator.create_voice(texts, submission)

        for image, voice in zip(images, voice):
            ffmpeg_base_video = ffmpeg_base_video.overlay(image.path)
