
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.compositing.concatenate import concatenate_videoclips

from BL.VideoConnector.IVideoConnector import IVideoConnector
from BL.VideoParts.BackgroundCreator.IBackgroundCreator import IBackgroundCreator
from BL.VideoParts.FrontCreator.TextCreatorManager.ITextCreatorManager import ITextCreatorManager
from Common.FileCommon import FileCommon
from Common.VoiceCommon import VoiceCommon
from Configurations.VideoConnectorConfiguration.VideoConnectorConfiguration import VideoConnectorConfiguration
from Pullers.BackgroundPuller.IBackgroundPuller import IBackgroundPuller


class TextVideoConnector(IVideoConnector):

    def __init__(self,
                 background_puller: IBackgroundPuller,
                 background_creator: IBackgroundCreator,
                 video_connector_config: VideoConnectorConfiguration,
                 text_puller: ITextCreatorManager
                 ):
        self.background_creator = background_creator
        self.config = video_connector_config
        self.text_puller = text_puller
        self.background_puller = background_puller

    def connect_video(self, voice: str, background: str):
        text_voice_video = self.background_puller.pull_background(voice, None)
        stt_models = self.text_puller.create_voice(text_voice_video)
        (composite, _) = VoiceCommon.composite_voice_from_audio_files([text_voice_video])
        images_clips = [stt_model.text_clip.set_duration(stt_model.end_time - stt_model.start_time
                                                 ).resize(width=int(self.config.width)
                                                          )
                        for stt_model in stt_models
                        ]
        image_concat = concatenate_videoclips(images_clips).set_position(
            (0, (self.config.height - images_clips[0].h) // 2)
        )

        image_concat.audio = composite
        video_background = self.background_creator.create_background(background, video_length=int(composite.duration)).background_data

        final = CompositeVideoClip([video_background, image_concat])

        FileCommon.save_dir(self.config.tmp_path)
        tmp_path = f"{self.config.tmp_path}{id(voice)}{self.config.file_format}"

        final.write_videofile(
            tmp_path,
            codec='h264_nvenc',

        )

        FileCommon.save_dir(self.config.result_path)

        return final
