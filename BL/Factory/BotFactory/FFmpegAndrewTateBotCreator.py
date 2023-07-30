from BL.Factory.BotFactory.BotFactoryBase import BotFactoryBase
from BL.VideoConnector.FFmpegVideoConnector import FFmpegVideoConnector
from BL.VideoConnector.IVideoConnector import IVideoConnector
from BL.VideoConnector.TextVideoConnector import TextVideoConnector
from BL.VideoParts.BackgroundCreator.BackgroundCreator import BackgroundCreator
from BL.VideoParts.BackgroundCreator.FFmpegBackgroundCreator import FFmpegBackgroundCreator
from BL.VideoParts.FrontCreator.FFMpegFrontCreator.FFMpegTextCreator.DrawText.DrawText import DrawText
from BL.VideoParts.FrontCreator.FFMpegFrontCreator.FFMpegTextCreator.DrawTextCreator import DrawTextCreator
from BL.VideoParts.FrontCreator.TextCreator.TextCreator import TextCreator
from BL.VideoParts.FrontCreator.TextCreatorManager.TextCreatorManager import TextCreatorManager
from Common.Factory.STTModelFactory.STTModelFactory import STTModelFactory
from Configurations.Configuration import Configuration
from Pullers.BackgroundPuller.VideoBackgroundPuller import VideoBackgroundPuller
from Pullers.FrontContentPuller.TextPuller.STTPuller.STTPullerProxy import STTPullerProxy
from Pullers.FrontContentPuller.TextPuller.STTPuller.WhisperSTTPuler import WhisperSTTPuller
from Pullers.VideoDonwloaderPuller.YoutubeVideoDownloaderPuller import YoutubeVideoDownloaderPuller


class FFmpegAndrewTateBotCreator(BotFactoryBase):

    def __init__(self, config: Configuration):
        super().__init__(config)

    def create_bot(self,) -> IVideoConnector:
        stt_model_factory = STTModelFactory()
        text_puller = WhisperSTTPuller(stt_model_factory)
        text_puller = STTPullerProxy(text_puller)
        downloader_puller = YoutubeVideoDownloaderPuller(self.config.background_configuration)
        background_puller = VideoBackgroundPuller(self.config.background_configuration, downloader_puller)
        background_creator = FFmpegBackgroundCreator(background_puller, self.config.video_connector_configuration)
        draw_text = DrawText()
        draw_text_creator = DrawTextCreator(text_puller, draw_text)

        text_video_connector = FFmpegVideoConnector(background_puller,
                                                    background_creator,
                                                    self.config.video_connector_configuration,
                                                    draw_text_creator,
                                                    downloader_puller)

        return text_video_connector
