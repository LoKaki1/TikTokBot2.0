from moviepy.video.io.VideoFileClip import VideoFileClip


class IBackgroundCreator:

    def create_background(self, background_name: str, video_length: int) -> VideoFileClip:
        """
        :return:
        """