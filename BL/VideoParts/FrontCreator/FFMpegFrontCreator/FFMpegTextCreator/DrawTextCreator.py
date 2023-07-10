from BL.VideoParts.FrontCreator.FFMpegFrontCreator.FFMpegTextCreator.DrawText.IDrawText import IDrawText
from Pullers.FrontContentPuller.TextPuller.STTPuller.ISTTPuller import ISTTPuller


class DrawTextCreator:

    def __init__(self,
                 stt_puller: ISTTPuller,
                 draw_text: IDrawText):
        self.stt_puller = stt_puller
        self.draw_text = draw_text

    def create_voice(self, path: str, ffmpeg_base=None):
        stt_models = self.stt_puller.pull_text_from_audio(path)

        return self.draw_text.draw_text(stt_models, ffmpeg_base)

