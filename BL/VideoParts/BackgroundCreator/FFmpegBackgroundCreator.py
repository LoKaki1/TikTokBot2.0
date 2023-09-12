import ffmpeg

from BL.VideoParts.BackgroundCreator.IBackgroundCreator import IBackgroundCreator
from Common.Models.BackgroundModel import BackgroundModel
from Configurations.VideoConnectorConfiguration.VideoConnectorConfiguration import VideoConnectorConfiguration
from Pullers.BackgroundPuller.IBackgroundPuller import IBackgroundPuller


class FFmpegBackgroundCreator(IBackgroundCreator):

    def __init__(self,
                 background_puller: IBackgroundPuller,
                 config: VideoConnectorConfiguration,
                 ):
        self.background_puller = background_puller
        self.config = config

    def create_background(self, background_name: str, video_length: int = None) -> BackgroundModel:
        background_path = self.background_puller.pull_background(background_name, video_length)

        background_result = ffmpeg.input(background_path)
        c = self.config.width // 2
        half_w = self.config.width // 2
        x1 = c - half_w
        x2 = c + half_w
        background_result = background_result.filter('scale', -1, self.config.height)

        background_result = background_result.crop(x2, 0, x2, self.config.height)

        return BackgroundModel(background_result)
