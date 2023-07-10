from typing import Union, Tuple

import ffmpeg
from moviepy.video.VideoClip import VideoClip
from moviepy.editor import ImageClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.compositing.concatenate import concatenate_videoclips

from BL.Factory.MetadataFactory.ImageTextFactory import ImageTextFactory
from BL.VideoConnector.ImageVoiceConnector.IImageVoiceConnector import IImageVoiceConnector
from BL.VideoParts.FrontCreator.ImageTextCreator.IImageTextCreator import IImageTextCreator
from BL.VideoParts.VoiceCreator.IVoiceCreator import IVoiceCreator
from Configurations.VideoConnectorConfiguration.VideoConnectorConfiguration import VideoConnectorConfiguration


class OverlayImages(IImageVoiceConnector):

    def __init__(self,
                 config: VideoConnectorConfiguration,
                 image_creator: IImageTextCreator,
                 voice_creator: IVoiceCreator,
                 image_text_factory: ImageTextFactory
                 ):
        self.image_text_factory = image_text_factory
        self.image_creator = image_creator
        self.voice_creator = voice_creator
        self.config = config

    def connect_image_voice(self,
                            submission: str,
                            number: int = None,
                            ffmpeg_base=None
                            ):
        [images, texts] = self.image_text_factory.create_images_text(submission, number)

        (audio_composite, audio_clips) = self.voice_creator.create_voice(texts, submission)

        end_time = 0

        for overlay, audio_clip in zip(images, audio_clips):
            start_time = end_time
            end_time += audio_clip.duration
            ffmpeg_base = ffmpeg_base.overlay(ffmpeg.input(overlay),
                                              enable=f'between(t, {start_time}, {end_time})',
                                              x='(main_w-overlay_w)/2 ', y='(main_h-overlay_h)/2',
                                              **{"[1:v]scale": f"{self.config.width}:-1 [ovrl]"}
                                              )

        return ffmpeg_base, audio_composite.duration
