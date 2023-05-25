import ffmpeg

from BL.VideoParts.BackgroundCreator.IBackgroundCreator import IBackgroundCreator
from Common.Models.BackgroundModel import BackgroundModel
from Pullers.BackgroundPuller.IBackgroundPuller import IBackgroundPuller


class FFmpegBackgroundCreator(IBackgroundCreator):

    def __init__(self, background_puller: IBackgroundPuller):
        self.background_puller = background_puller

    def create_background(self, background_name: str, video_length: int) -> BackgroundModel:
        background_path = self.background_puller.pull_background(background_name, video_length)
        background_result = ffmpeg.input(background_path)

        return BackgroundModel(background_result)
