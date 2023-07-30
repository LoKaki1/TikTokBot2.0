import os
from os import path

from pytube import YouTube
from pytube.cli import on_progress

from Common.RegularCommon.RegularCommon import split_youtube_url
from Configurations.BackgroundConfiguration.BackgroundConfiguration import BackgroundConfiguration
from Pullers.VideoDonwloaderPuller.IVideoDownloaderPuller import IVideoDownloaderPuller


class YoutubeVideoDownloaderPuller(IVideoDownloaderPuller):

    def __init__(self, config: BackgroundConfiguration):
        self.config = config

    def download_video(self, url: str) -> str:
        background = split_youtube_url(url)
        background_path = f"{self.config.background_folder}{background}{self.config.background_format}"

        if not path.exists(self.config.background_folder):
            os.makedirs(self.config.background_folder)

        if not path.exists(background_path):
            youtube = YouTube(url,
                              on_progress_callback=on_progress,
                              use_oauth=True,
                              allow_oauth_cache=True)

            streams = youtube.streams.get_highest_resolution()
            streams.download(self.config.background_folder, filename=f"{background}{self.config.background_format}")

        return background_path
