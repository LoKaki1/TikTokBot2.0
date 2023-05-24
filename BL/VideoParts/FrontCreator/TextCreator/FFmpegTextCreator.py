from moviepy.video.VideoClip import TextClip

from BL.VideoParts.FrontCreator.TextCreator.ITextCreator import ITextCreator


class FFmpegTextCreator(ITextCreator):

    def create_text(self, text: str, duration: float) -> TextClip:
        pass
