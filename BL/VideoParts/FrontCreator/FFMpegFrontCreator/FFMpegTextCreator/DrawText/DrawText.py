from tensorboard.plugins.text.summary_v2 import text_pb

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
            t = text_model.start_time
            # 3t -2start = end
            # t = (end + 2start) / 3
            # 50 * t (1 + 2) * (t - text_model.start_time)
            # 50 * (1 + 2(math_term -text_model.start_time))
            duration_multiplication = 12.6 / text_model.duration
            while t - text_model.start_time < text_model.end_time - text_model.start_time:
                # if t-text_model.start_time < (text_model.end_time - t) / 2:
                #     print(50 * (1 + 2 * (t - text_model.start_time)))
                # else:
                #     print((50 * (1 + 2 * (t - text_model.start_time)) / (1 + (t - (text_model.end_time - text_model.start_time * 2) / 3))))
                # math_term = (text_model.end_time + text_model.start_time * 2) / 3
                # what = 50 * (1 + 2 * (math_term - text_model.start_time))
                # data = round(50 * 2 * (1 + 2 * (t - text_model.start_time)))\
                #     if t - text_model.start_time < (text_model.end_time - t) / 2\
                #     else round(50 / (1 + 2 * (t - math_term)) + (what - 50))
                # p = 12.6 / (text_model.duration) * (t - text_model.start_time)
                # data = - p ** 3 + 12*p**2 +10 * p + 30
                data = round(-(duration_multiplication * (t - text_model.start_time)) * (duration_multiplication * (t - text_model.start_time)) * (duration_multiplication * (t - text_model.start_time)) + 12 * (duration_multiplication * (t - text_model.start_time)) * (duration_multiplication * (t - text_model.start_time)) + 10 * (duration_multiplication * (t - text_model.start_time)) + 30)
                print(data)
                t += 0.01
            print('chips')
            ffmpeg_base = ffmpeg_base.drawtext(text,

                                               fontcolor='#FFFFFF',
                                               fontfile=r'C:/WINDOWS/fonts/CascadiaCode.ttf',
                                               enable=f'between(t, {text_model.start_time}, {text_model.end_time})',
                                               # fontsize=f'if(lt(t - {text_model.start_time}, ({text_model.end_time} - '
                                               #          f'{text_model.start_time}) / 2), 120 + (t - {text_model.start_time}), '
                                               #          f'120 - (t - {text_model.start_time}))',
                                               # fontsize=f'(t - {text_model.start_time}) ^ 3 - 2 * (t - {text_model.start_time}) + 220',
                                               fontsize=f'round(-({duration_multiplication} * (t - {text_model.start_time})) * ({duration_multiplication} * (t - {text_model.start_time})) * ({duration_multiplication} * (t - {text_model.start_time})) + 12 * ({duration_multiplication} * (t - {text_model.start_time})) * ({duration_multiplication} * (t - {text_model.start_time})) + 10 * ({duration_multiplication} * (t - {text_model.start_time})) + 30)',
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
