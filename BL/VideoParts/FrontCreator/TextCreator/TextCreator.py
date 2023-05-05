from moviepy.video.VideoClip import TextClip

from BL.VideoParts.FrontCreator.TextCreator.ITextCreator import ITextCreator


class TextCreator(ITextCreator):

    def create_text(self, text: str, duration: float) -> TextClip:
        text_clip = TextClip(text, color='white', stroke_color='red', fontsize=75
                             ).set_position('center').set_duration(duration)

        return text_clip
