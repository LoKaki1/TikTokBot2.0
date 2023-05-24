import ffmpeg
from ffmpeg.nodes import Node

from Common.LoggerCommon.Logger import log_info
from Pullers.FrontContentPuller.TextPuller.STTPuller.WhisperSTTPuler import WhisperSTTPuller

whisper_something = WhisperSTTPuller()
texts = whisper_something.pull_text_from_audio('./assets/videos/short.mp4')
video = ffmpeg.input('./assets/videos/short.mp4')
for text in texts:
    log_info(text)
    video = video.drawtext(text.text,
                           fontsize=30,

                           fontfile=r'C:\Users\meir\anaconda3\envs\PycharmProjects\Lib\site-packages\matplotlib\mpl-data'
                                    r'\fonts\ttf\cmmi10.ttf',
                           enable=f'between(t,{text.start_time},{text.end_time})')

video.output(f'{id(video)}.mp4').run()
# (
#     ffmpeg
#         .input('./assets/videos/short.mp4')
#         .drawtext("hi",
#                   fontsize=60,
#                   fontfile=r'C:\Users\meir\anaconda3\envs\PycharmProjects\Lib\site-packages\matplotlib\mpl-data\fonts\ttf\cmmi10.ttf',
#                   enable='between(t,0,4)').output('result.mp4').run()
# )
