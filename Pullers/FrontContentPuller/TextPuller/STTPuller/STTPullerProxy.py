from typing import List

from Common.Models.STTModel import STTModel
from Pullers.FrontContentPuller.TextPuller.STTPuller.ISTTPuller import ISTTPuller


class STTPullerProxy(ISTTPuller):

    def __init__(self,
                 stt_puller: ISTTPuller):
        self.stt_puller = stt_puller

    def pull_text_from_audio(self, path: str) -> List[STTModel]:
        stt_models = self.stt_puller.pull_text_from_audio(path)
        last = STTModel("", 0, stt_models[0].start_time, 0)
        new = []

        for index, model in enumerate(stt_models):
            current = stt_models[index]

            if len(last + current) < 11:
                last += current
            else:
                new.append(last)
                last = current

        if last not in new:
            new.append(last)

        return new

