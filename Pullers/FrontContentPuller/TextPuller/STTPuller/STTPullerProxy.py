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
        # new_models = []
        # index = 0
        #
        # for model in stt_models:
        #     if len(model) > 16:
        #         new_models[index] = model
        #         index += 1
        #
        #         continue
        #
        #     if len(new_models) > index:
        #         if new_models[index] + model <= 16:
        #             new_models[index] += model
        #         else:
        #             index += 1
        #     else:
        #

        # new_model = STTModel("", 0, 0, 0)
        # new_model.text = ""
        # proxy_models = []
        #
        # for model in stt_models:
        #     if len(new_model.text) > 16:
        #         proxy_models.append(new_model)
        #         new_model = model.clone()
        #         new_model.text = ""
        #
        #     if len(model.text) > 16:
        #         proxy_models.append(new_model)
        #         new_model = model.clone()
        #         new_model.text = ""
        #         proxy_models.append(model)
        #
        #     if len(model.text + new_model.text) > 16:
        #         proxy_models.append(new_model)
        #         new_model = model.clone()
        #         new_model.text = ""
        #     else:
        #         new_model += model
        #
        # if new_model not in proxy_models:
        #     proxy_models.append(new_model)
        #
        return proxy_models
