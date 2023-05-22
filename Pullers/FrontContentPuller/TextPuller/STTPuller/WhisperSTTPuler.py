from typing import List

from Common.LoggerCommon.Logger import logger_info_decorator
from Common.Models.STTModel import STTModel
from Pullers.FrontContentPuller.TextPuller.STTPuller.ISTTPuller import ISTTPuller
import whisper


class WhisperSTTPuller(ISTTPuller):

    @logger_info_decorator
    def pull_text_from_audio(self, path: str) -> List[STTModel]:
        model = whisper.load_model("base", device='cpu')
        result = model.transcribe(path, word_timestamps=True)

        segments = result['segments'][0:len(result['segments'])]
        stt_models = []

        for segment in segments:
            words = segment['words']

            for index in range(0, len(words), 2):
                # if index >= len(words) - 2:
                #     (start, end) = word['start'], word['end']
                # else:
                #     (start, end) = word['start'], words[index + 1]['end']
                new_words = words[index: index + 2]
                (start, end) = new_words[0]['start'], new_words[-1]['end']

                text = ' '.join([new_word['word'] for new_word in new_words])
                stt_models.append(
                    STTModel(
                        text,
                        end - start,
                        start,
                        end
                    )
                )

        return stt_models
