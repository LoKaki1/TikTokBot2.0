from tensorboard.plugins.text.summary_v2 import text_pb

from BL.VideoParts.FrontCreator.FFMpegFrontCreator.FFMpegTextCreator.DrawText.IDrawText import IDrawText
from Common.Models.STTModel import STTModel
def calc_parabola_vertex(x1, y1, x2, y2, x3, y3):
    '''
		Adapted and modifed to get the unknowns for defining a parabola:
		http://stackoverflow.com/questions/717762/how-to-calculate-the-vertex-of-a-parabola-given-three-points
		'''
    denom = (x1 - x2) * (x1 - x3) * (x2 - x3)
    if denom == 0:
        return 0, 0, base_size
    A = (x3 * (y2 - y1) + x2 * (y1 - y3) + x1 * (y3 - y2)) / denom
    B = (x3 * x3 * (y1 - y2) + x2 * x2 * (y3 - y1) + x1 * x1 * (y2 - y3)) / denom
    C = (x2 * x3 * (x2 - x3) * y1 + x3 * x1 * (x3 - x1) * y2 + x1 * x2 * (x1 - x2) * y3) / denom
    print(A, B, C)
    return round(A), round(B), round(C)


base_size = 30
max_size = 60

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
            a, b, c = calc_parabola_vertex(x1, y1, x2, y2, x3, y3)

            print(f'{a} * (t - {text_model.start_time}) * (t - {text_model.start_time}) + {b} * (t - {text_model.start_time}) + {c}')
            ffmpeg_base = ffmpeg_base.drawtext(text,
                                               fontcolor='#FFFFFF',
                                               fontfile=r'C:/WINDOWS/fonts/CascadiaCode.ttf',
                                               enable=f'between(t, {text_model.start_time}, {text_model.end_time})',
                                               # fontsize=f'if(lt(t - {text_model.start_time}, ({text_model.end_time} - '
                                               #          f'{text_model.start_time}) / 2), 120 + (t - {text_model.start_time}), '
                                               # fontsize=f'(t - {text_model.start_time}) ^ 3 - 2 * (t - {text_model.start_time}) + 220',
                                               # fontsize=f'round(-({duration_multiplication} * (t - {text_model.start_time})) * ({duration_multiplication} * (t - {text_model.start_time})) * ({duration_multiplication} * (t - {text_model.start_time})) + 12 * ({duration_multiplication} * (t - {text_model.start_time})) * ({duration_multiplication} * (t - {text_model.start_time})) + 10 * ({duration_multiplication} * (t - {text_model.start_time})) + 30)',

                                               # fontsize=f'{a} * (t - {text_model.start_time})*(t - {text_model.start_time})  + {b}*(t - {text_model.start_time}) + {c}',
                                               fontsize=f'{a}*(t - {text_model.start_time})*(t - {text_model.start_time}) + {b}*(t - {text_model.start_time}) + {c}',
                                               x='(w-text_w)/2', y='(h-text_h)/2',
                                               # x='if(lt(t-0.5,0),-text_w + ((w-text_w)/2 -(-text_w))*t/0.5,(w-text_w)/2)',
                                               # x=f'-text_w + ((w-text_w)/2 -(-text_w))*(t-{text_model.start_time})/0.5',
                                               # y='(h-text_h)-10',
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
