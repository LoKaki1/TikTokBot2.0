import math

from BL.VideoParts.FrontCreator.FFMpegFrontCreator.FFMpegTextCreator.DrawText.IDrawText import IDrawText
from Common.LoggerCommon.Logger import log_info
from Common.Models.STTModel import STTModel
from Common.RegularCommon.RegularCommon import calc_parabola_vertex, calc_parabolla_function_from_3_points

base_size = 83
max_size = 90


class DrawText(IDrawText):

    def __init__(self):
        """
        Should add draw text to config or to init
        """
    def draw_text(self, text_models, ffmpeg_base=None):
        for text_model in text_models:
            text = self.get_text(text_model).title()

            x1, y1 = (0, base_size)
            x2, y2 = (text_model.duration / 2, max_size)
            x3, y3 = (text_model.duration, base_size)
            x = f'(t-{text_model.start_time})'
            st = calc_parabolla_function_from_3_points(x1, y1, x2, y2, x3, y3, x)
            log_info(st)
            ffmpeg_base = ffmpeg_base.drawtext(text,
                                               fontcolor='#fffbde',
                                               fontfile='./assets/fonts/THEBOLDFONT.ttf',
                                               enable=f'between(t, {text_model.start_time}, {text_model.end_time})',
                                               fontsize=f'{st}',
                                               x='(w-text_w)/2', y='(h-text_h)/2',
                                               shadowcolor='#000000',
                                               shadowx=10,
                                               shadowy=10
                                               )

        return ffmpeg_base

    def get_text(self, text_model: STTModel) -> str:
        return "".join(c for c in text_model.text if c.isalpha() or c == ' ')

