import ffmpeg
import torch

from Configurations.ConfigurationLoader import load_configuration
from Pullers.BackgroundPuller.VideoBackgroundPuller import VideoBackgroundPuller
from Pullers.FrontContentPuller.TextPuller.STTPuller.WhisperSTTPuler import WhisperSTTPuller

print(torch.cuda.is_available())
text_puller = WhisperSTTPuller()
config = load_configuration('./Configurations/config.json')
pull_background = VideoBackgroundPuller(config.background_configuration)
pull_background.pull_background('andrewTate')
#
# texts_pulled = text_puller.pull_text_from_audio('./assets/videos/short.mp4')
# video = ffmpeg.input('./assets/videos/short.mp4')
# for text in texts_pulled:
#     video = video.drawtext(text.text,
#                            fontsize=70,
#                            enable=f'between(t, {text.start_time}, {text.end_time})',
#
#                            x=40,
#                            y=1080 / 2
#                            )
#
# video.output(f'{id(video)}.mp4',  vcodec='h264_nvenc').run()
