from moviepy.video.io.VideoFileClip import VideoFileClip

from Common.Models.BackgroundModel import BackgroundModel


class IBackgroundCreator:

    def create_background(self, background_name: str, video_length: int) -> BackgroundModel:
        """
        :return:
        """