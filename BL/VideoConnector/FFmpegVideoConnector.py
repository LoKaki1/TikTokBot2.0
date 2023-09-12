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

    def connect_video(self, voice: str, background: str, use_voice_as_background: bool = False):

        text_voice_video = self.video_downloader.download_video(voice, )
        text_voice_video = self.background_puller.chop_video(text_voice_video, )
        (composite, _) = VoiceCommon.composite_voice_from_audio_files([text_voice_video])
        if use_voice_as_background:
            ffmpeg_base = self.background_creator.create_background(text_voice_video, None).background_data
        else:
            ffmpeg_base = self.background_creator.create_background(background, int(composite.duration)).background_data
        ffmpeg_base = self.draw_text_creator.create_voice(text_voice_video, ffmpeg_base)
        audio = ffmpeg.input(text_voice_video)
        ffmpeg_result = ffmpeg.concat(ffmpeg_base, audio, v=1, a=1)

        return self.ffmpeg_render.render_ffmpeg_output(ffmpeg_result)
