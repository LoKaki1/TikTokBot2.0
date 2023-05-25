from moviepy.video.io.VideoFileClip import VideoFileClip

from BL.VideoParts.BackgroundCreator.IBackgroundCreator import IBackgroundCreator
from Common.LoggerCommon.Logger import logger_info_decorator
from Common.Models.BackgroundModel import BackgroundModel
from Configurations.VideoConnectorConfiguration.VideoConnectorConfiguration import VideoConnectorConfiguration
from Pullers.BackgroundPuller.IBackgroundPuller import IBackgroundPuller


class BackgroundCreator(IBackgroundCreator):

    def __init__(self,
                 background_puller: IBackgroundPuller,
                 config: VideoConnectorConfiguration,
                 ):
        self.background_puller = background_puller
        self.config = config

    @logger_info_decorator
    def create_background(self, background_name: str, video_length: int) -> BackgroundModel:
        """
        :return:
        """
        background_path = self.background_puller.pull_background(background_name, video_length)
        clip = VideoFileClip(background_path) \
            .without_audio() \
            .resize(height=self.config.height)

        # calculate the center of the background clip
        c = clip.w // 2

        # calculate the coordinates where to crop
        half_w = self.config.width // 2
        x1 = c - half_w
        x2 = c + half_w

        background_clip = clip.crop(x1=x1, y1=0, x2=x2, y2=self.config.height)
        background_model = BackgroundModel(background_clip)

        return background_model
