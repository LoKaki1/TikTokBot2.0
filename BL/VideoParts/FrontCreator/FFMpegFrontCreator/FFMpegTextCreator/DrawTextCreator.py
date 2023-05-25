from Pullers.FrontContentPuller.TextPuller.STTPuller.ISTTPuller import ISTTPuller


class DrawTextCreator:

    def __init__(self,
                 stt_puller: ISTTPuller):
        self.stt_puller = stt_puller

    def create_voice(self, path: str, ffmpeg_base=None):
        stt_models = self.stt_puller.pull_text_from_audio(path)

        for stt_model in stt_models:
            ffmpeg_base = ffmpeg_base.drawtext(("".join(c for c in stt_model.text if c.isalpha() or c == ' ')).title(),
                                               fontsize=120,
                                               fontcolor='#FFFFFF',
                                               fontfile=r'C:/WINDOWS/fonts/CascadiaCode.ttf',
                                               enable=f'between(t, {stt_model.start_time}, {stt_model.end_time})',
                                               x='(w-text_w)/2', y='(h-text_h)/2',
                                               shadowcolor='#000000',
                                               shadowx=5,
                                               shadowy=5
                                               )


        return ffmpeg_base
