
import ffmpeg

from BL.VideoConnector.IVideoConnector import IVideoConnector
from BL.VideoParts.BackgroundCreator.IBackgroundCreator import IBackgroundCreator
from BL.VideoParts.FrontCreator.FFMpegFrontCreator.FFMpegTextCreator.DrawTextCreator import DrawTextCreator
from Common.VoiceCommon import VoiceCommon
from Configurations.VideoConnectorConfiguration.VideoConnectorConfiguration import VideoConnectorConfiguration
from Pullers.BackgroundPuller.IBackgroundPuller import IBackgroundPuller


class FFmpegVideoConnector(IVideoConnector):

    def __init__(self,
                 background_puller: IBackgroundPuller,
                 background_creator: IBackgroundCreator,
                 video_connector_config: VideoConnectorConfiguration,
                 draw_text_creator: DrawTextCreator
                 ):
        self.draw_text_creator = draw_text_creator
        self.background_creator = background_creator
        self.config = video_connector_config
        self.background_puller = background_puller

    def connect_video(self, voice: str, background: str):
        text_voice_video = self.background_puller.pull_background(voice, None)
        (composite, _) = VoiceCommon.composite_voice_from_audio_files([text_voice_video])
        ffmpeg_base = self.background_creator.create_background(background, int(composite.duration)).background_data
        ffmpeg_base = self.draw_text_creator.create_voice(text_voice_video, ffmpeg_base)
        audio = ffmpeg.input(text_voice_video)
        result_path = f"{self.config.result_path}{id(voice)}{self.config.file_format}"
        ffmpeg_result = ffmpeg.concat(ffmpeg_base, audio, v=1, a=1)

        return ffmpeg_result.output(result_path).run()
        # images_clips = [stt_model.text_clip.set_duration(stt_model.end_time - stt_model.start_time
        #                                          ).resize(width=int(self.config.width)
        #                                                   )
        #                 for stt_model in stt_models
        #                 ]
        # image_concat = concatenate_videoclips(images_clips).set_position(
        #     (0, (self.config.height - images_clips[0].h) // 2)
        # )
        #
        # image_concat.audio = composite
        # video_background = self.background_creator.create_background(background, video_length=int(composite.duration)).background_data
        #
        # final = CompositeVideoClip([video_background, image_concat])
        #
        # FileCommon.save_dir(self.config.result_path)
        # result_path = f"{self.config.result_path}{id(voice)}{self.config.file_format}"
        #
        # final.write_videofile(
        #     result_path,
        #     codec='h264_nvenc',
        #
        # )
        #
        # FileCommon.save_dir(self.config.result_path)

