from os import path
from random import randrange

from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from pytube import YouTube
from pytube.cli import on_progress

from Common.LoggerCommon.Logger import logger_info_decorator
from Configurations.BackgroundConfiguration.BackgroundConfiguration import BackgroundConfiguration
from Pullers.BackgroundPuller.IBackgroundPuller import IBackgroundPuller


class VideoBackgroundPuller(IBackgroundPuller):

    def __init__(self, config: BackgroundConfiguration):
        self.config = config

    @logger_info_decorator
    def pull_background(self, video_name: str, video_length: int) -> str:
        """
        :return:
        """
        background_video_path = self._download_background(video_name)
        chopped_video = self._chop_background_video(background_video_path, video_name, video_length)

        return chopped_video

    def _download_background(self, background: str) -> str:
        background_path = f"{self.config.background_folder}{background}{self.config.background_format}"

        if not path.exists(background_path):
            YouTube(self.config.background_type[background],
                    on_progress_callback=on_progress) \
                .streams.filter(res=self.config.background_resolution
                                ).first().download(self.config.background_folder,
                                                   filename=f'{background}{self.config.background_format}')

        return background_path

    def _chop_background_video(self,
                               background_path: str,
                               background_name: str,
                               length: int = None
                               ) -> str:
        video_duration = int(VideoFileClip(background_path).duration)
        start_time, end_time = ((random_time := randrange(0, video_duration)), random_time + length)

        chopped_video_path = f'{self.config.chopped_video_folder}/{background_name}{self.config.background_format}'

        try:
            ffmpeg_extract_subclip(
                background_path,
                start_time,
                end_time,
                targetname=chopped_video_path
            )

        except (OSError, IOError):  # ffmpeg issue see #348

            with VideoFileClip(background_path) as video:
                new = video.subclip(start_time, end_time)
                new.write_videofile(chopped_video_path)

        return chopped_video_path
