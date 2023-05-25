from BL.Factory.BotFactory.BotFactoryBase import BotFactoryBase
from BL.VideoConnector.FFmpegVideoConnector import FFmpegVideoConnector
from BL.VideoConnector.IVideoConnector import IVideoConnector
from BL.VideoConnector.TextVideoConnector import TextVideoConnector
from BL.VideoParts.BackgroundCreator.BackgroundCreator import BackgroundCreator
from BL.VideoParts.BackgroundCreator.FFmpegBackgroundCreator import FFmpegBackgroundCreator
from BL.VideoParts.FrontCreator.FFMpegFrontCreator.FFMpegTextCreator.DrawTextCreator import DrawTextCreator
from BL.VideoParts.FrontCreator.TextCreator.TextCreator import TextCreator
from BL.VideoParts.FrontCreator.TextCreatorManager.TextCreatorManager import TextCreatorManager
from Configurations.Configuration import Configuration
from Pullers.BackgroundPuller.VideoBackgroundPuller import VideoBackgroundPuller
from Pullers.FrontContentPuller.TextPuller.STTPuller.WhisperSTTPuler import WhisperSTTPuller


class FFmpegAndrewTateBotCreator(BotFactoryBase):

    def __init__(self, config: Configuration):
        super().__init__(config)

    def create_bot(self,) -> IVideoConnector:
        text_puller = WhisperSTTPuller()
        background_puller = VideoBackgroundPuller(self.config.background_configuration)
        background_creator = FFmpegBackgroundCreator(background_puller, self.config.video_connector_configuration)
        draw_text = DrawTextCreator(text_puller)
        text_video_connector = FFmpegVideoConnector(background_puller, background_creator, self.config.video_connector_configuration, draw_text)

        return text_video_connector
