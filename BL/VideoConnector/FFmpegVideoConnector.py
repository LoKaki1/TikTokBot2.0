import subprocess

import ffmpeg

from BL.VideoConnector.IVideoConnector import IVideoConnector
from BL.VideoParts.BackgroundCreator.IBackgroundCreator import IBackgroundCreator
from BL.VideoParts.FrontCreator.FFMpegFrontCreator.FFMpegTextCreator.DrawTextCreator import DrawTextCreator
from Common.FFmpegExtensions.FFmpegRender.IFFmpegRender import IFFmpegRender
from Common.LoggerCommon.Logger import log_info
from Common.VoiceCommon import VoiceCommon
from Configurations.VideoConnectorConfiguration.VideoConnectorConfiguration import VideoConnectorConfiguration
from Pullers.BackgroundPuller.IBackgroundPuller import IBackgroundPuller
from Pullers.VideoDonwloaderPuller.IVideoDownloaderPuller import IVideoDownloaderPuller


class FFmpegVideoConnector(IVideoConnector):

    def __init__(self,
                 background_puller: IBackgroundPuller,
                 background_creator: IBackgroundCreator,
                 video_connector_config: VideoConnectorConfiguration,
                 draw_text_creator: DrawTextCreator,
                 video_downloader: IVideoDownloaderPuller,
                 ffmpeg_render: IFFmpegRender
                 ):
        self.ffmpeg_render = ffmpeg_render
        self.video_downloader = video_downloader
        self.draw_text_creator = draw_text_creator
        self.background_creator = background_creator
        self.config = video_connector_config
        self.background_puller = background_puller

    def connect_video(self, voice: str, background: str):
        text_voice_video = self.video_downloader.download_video(voice, )
        text_voice_video = self.background_puller.chop_video(text_voice_video, )
        (composite, _) = VoiceCommon.composite_voice_from_audio_files([text_voice_video])
        ffmpeg_base = self.background_creator.create_background(background, int(composite.duration)).background_data
        ffmpeg_base = self.draw_text_creator.create_voice(text_voice_video, ffmpeg_base)
        audio = ffmpeg.input(text_voice_video)
        ffmpeg_result = ffmpeg.concat(ffmpeg_base, audio, v=1, a=1)

        return self.ffmpeg_render.render_ffmpeg_output(ffmpeg_result)
        # result_path = f"{self.config.result_path}{id(voice)}{self.config.file_format}"
        # output = ffmpeg_result.output(result_path, vcodec='h264_nvenc')
        #
        # compiled = output.compile()
        # # return output.run()
        # filter_complex = compiled.index('-filter_complex')
        # all_of_filters = compiled[filter_complex + 1]
        # script_file = f'./assets/ffmpeg_files/{id(voice)}'
        # with open(script_file, 'w') as file:
        #     file.write(all_of_filters)
        #
        # compiled_copy = compiled.copy()
        # compiled_copy[filter_complex] = '-filter_complex_script'
        # compiled_copy[filter_complex + 1] = script_file
        #
        # return subprocess.Popen(compiled_copy, stdin=None,
        #                         stdout=None,
        #                         stderr=None,
        #                         cwd=None, )
