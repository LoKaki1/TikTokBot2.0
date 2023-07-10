from typing import List

from Common.LoggerCommon.Logger import logger_info_decorator
from Common.Models.STTModel import STTModel
from Pullers.FrontContentPuller.TextPuller.STTPuller.ISTTPuller import ISTTPuller
import whisper


class WhisperSTTPuller(ISTTPuller):

    @logger_info_decorator
    def pull_text_from_audio(self, path: str) -> List[STTModel]:
        model = whisper.load_model("base",)
        result = model.transcribe(path, word_timestamps=True)

        segments = result['segments'][0:len(result['segments'])]
        stt_models = []

        for segment in segments:
            words = segment['words']
            multiple_words = STTModel("", 0, words[0]['start'], 0)

            for word in words:
                if len(multiple_words.text + word['word']) < 16:
                    multiple_words.text += word['word']
                    multiple_words.end_time = word['end']
                    multiple_words.duration = multiple_words.end_time - multiple_words.start_time

                else:
                    if multiple_words.text:
                        stt_models.append(multiple_words)

                    if len(word['word']) < 16:
                        multiple_words = STTModel(word['word'], ((end := word['end']) - (start := word['start'])), start, end)

                    else:
                        stt_models.append(STTModel(word['word'], ((end := word['end']) - (start := word['start'])), start, end))

                # if
                # if len(word['word']) > 16:
                #     stt_model = STTModel(word['word'],
                #                          (start := word['start'] - (end := word['end'])),
                #                          start,
                #                          end)
                #     stt_models.append(stt_model)
                #
                #     continue

                # new_words = words[index: index + 2]
                # (start, end) = new_words[0]['start'], new_words[-1]['end']
            #
            # for index in range(0, len(words), 2):
            #     new_words = words[index: index + 2]
            #     (start, end) = new_words[0]['start'], new_words[-1]['end']
            #
            #     text = ' '.join([new_word['word'] for new_word in new_words])
            #     stt_models.append(
            #         STTModel(
            #             text,
            #             end - start,
            #             start,
            #             end
            #         )
            #     )

        return stt_models
