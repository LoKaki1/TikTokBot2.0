from typing import Union, Tuple

from moviepy.video.VideoClip import VideoClip
from moviepy.editor import ImageClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.compositing.concatenate import concatenate_videoclips

from BL.VideoConnector.ImageVoiceConnector.IImageVoiceConnector import IImageVoiceConnector
from BL.VideoParts.FrontCreator.ImageTextCreator.IImageTextCreator import IImageTextCreator
from BL.VideoParts.VoiceCreator.IVoiceCreator import IVoiceCreator
from Configurations.VideoConnectorConfiguration.VideoConnectorConfiguration import VideoConnectorConfiguration


class ImageVoiceConnector(IImageVoiceConnector):

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
                            ) -> Tuple[Union[VideoClip, CompositeVideoClip], float]:
        images_texts = self.image_creator.create_image_text(submission)

        images = [image_text.path for image_text in images_texts]
        texts = [image_text.text for image_text in images_texts]

        (audio_composite, audio_clips) = self.voice_creator.create_voice(texts, submission)

        images_clips = [ImageClip(image
                                  ).set_duration(audio_clip.duration
                                                 ).resize(width=int(self.config.width)
                                                          ).crossfadein(self.config.fade_in
                                                                        ).crossfadeout(self.config.fade_out)
                        for image, audio_clip in zip(images, audio_clips)
                        ]
        image_concat = concatenate_videoclips(images_clips).set_position(
            (0, self.config.height // 2)
        )

        image_concat.audio = audio_composite

        return image_concat, audio_composite.duration
