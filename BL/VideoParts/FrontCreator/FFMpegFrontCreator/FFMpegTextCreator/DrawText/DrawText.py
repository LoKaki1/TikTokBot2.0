from BL.VideoParts.FrontCreator.FFMpegFrontCreator.FFMpegTextCreator.DrawText.IDrawText import IDrawText
from Common.Models.STTModel import STTModel


class DrawText(IDrawText):

    def __init__(self):
        """
        Should add draw text to config or to init
        """
    def draw_text(self, text_models, ffmpeg_base=None):
        for text_model in text_models:
            text = self.get_text(text_model).title()
            ffmpeg_base = ffmpeg_base.drawtext(text,
                                               fontsize=80,
                                               fontcolor='#FFFFFF',
                                               fontfile=r'C:/WINDOWS/fonts/CascadiaCode.ttf',
                                               enable=f'between(t, {text_model.start_time}, {text_model.end_time})',
                                               x='(w-text_w)/2', y='(h-text_h)/2',
                                               shadowcolor='#000000',
                                               shadowx=5,
                                               shadowy=5
                                               )

        return ffmpeg_base

    def get_text(self, text_model: STTModel) -> str:
        return "".join(c for c in text_model.text if c.isalpha() or c == ' ')
    #
    # def add_line(self, text: str) -> str:
    #     if len(text) <= 19:
    #         return text
    #
    #     texts = text.split(' ')
    #     data = []
    #     big_word = ""
    #
    #     for word in texts:
    #         if len((big_word + ' ' + word)) > 19:
    #             data.append(big_word)
    #             big_word = word
    #
    #         else:
    #             big_word += ' ' + word
    #     if big_word not in data:
    #         data.append(big_word)
    #     return '\n'.join(data)
