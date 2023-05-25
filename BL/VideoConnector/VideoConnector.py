import multiprocessing
import os

from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

from BL.VideoConnector.IVideoConnector import IVideoConnector
from BL.VideoConnector.ImageVoiceConnector.IImageVoiceConnector import IImageVoiceConnector
from BL.VideoParts.BackgroundCreator.IBackgroundCreator import IBackgroundCreator
from BL.VideoParts.FrontCreator.ImageTextCreator.IImageTextCreator import IImageTextCreator
from BL.VideoParts.VoiceCreator.IVoiceCreator import IVoiceCreator
from Common.FileCommon import FileCommon
from Common.LoggerCommon.Logger import logger_info_decorator
from Configurations.VideoConnectorConfiguration.VideoConnectorConfiguration import VideoConnectorConfiguration


class VideoConnector(IVideoConnector):

    def __init__(self,
                 video_connector_config: VideoConnectorConfiguration,
                 background_creator: IBackgroundCreator,
                 image_voice_connector: IImageVoiceConnector
                 ):
        self.image_voice_connector = image_voice_connector
        self.background_creator = background_creator
        self.config = video_connector_config

    @logger_info_decorator
    def connect_video(self,
                      submission: str,
                      background: str
                      ):
        """
        :return:
        """
        final = self._create_final_composite(submission, background)

        FileCommon.save_dir(self.config.tmp_path)
        tmp_path = f"{self.config.tmp_path}{submission}{self.config.file_format}"

        final.write_videofile(
            tmp_path,
            fps=self.config.fps,
            audio_codec=self.config.audio_codec,
            audio_bitrate=self.config.audio_bitrate,
            verbose=False,
            threads=multiprocessing.cpu_count()
        )

        FileCommon.save_dir(self.config.result_path)
        
        final_video_path = f"{self.config.result_path}{submission}{self.config.file_format}"

        ffmpeg_extract_subclip(
            tmp_path,
            0,
            final.duration,
            targetname=final_video_path,

        )

    def _create_final_composite(self,
                                submission: str,
                                background: str
                                ):
        image_voice_video, duration = self.image_voice_connector.connect_image_voice(submission)
        background = self.background_creator.create_background(
            background,
            int(duration)
        ).background_data

        final = CompositeVideoClip([background, image_voice_video])
        final.duration = duration

        return final
