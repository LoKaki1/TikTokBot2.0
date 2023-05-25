from typing import Union, Tuple

from moviepy.video.VideoClip import VideoClip
from moviepy.editor import ImageClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.compositing.concatenate import concatenate_videoclips

from BL.VideoConnector.ImageVoiceConnector.IImageVoiceConnector import IImageVoiceConnector
from BL.VideoParts.FrontCreator.ImageTextCreator.IImageTextCreator import IImageTextCreator
from BL.VideoParts.VoiceCreator.IVoiceCreator import IVoiceCreator
from Configurations.VideoConnectorConfiguration.VideoConnectorConfiguration import VideoConnectorConfiguration


class OverlayImages(IImageVoiceConnector):

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
                            ffmpeg_base=None
                            ):
        images_texts = self.image_creator.create_image_text(submission)

        images = [image_text.path for image_text in images_texts]
        texts = [image_text.text for image_text in images_texts]

        (audio_composite, audio_clips) = self.voice_creator.create_voice(texts, submission)

        end_time = 0

        for overlay, audio_clip in zip(images, audio_clips):
            start_time = end_time
            end_time += audio_clip.duration
            ffmpeg_base = ffmpeg_base.overlay(overlay,
                                              enable=f'between(t, {start_time}, {end_time})',
                                              x=40,
                                              y=1080 / 2
                                              )

        return ffmpeg_base, audio_composite.duration
