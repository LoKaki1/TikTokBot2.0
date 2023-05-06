from BL.Factory.BotFactory.BotFactoryBase import BotFactoryBase
from BL.VideoConnector.IVideoConnector import IVideoConnector
from BL.VideoConnector.TextVideoConnector import TextVideoConnector
from BL.VideoParts.BackgroundCreator.BackgroundCreator import BackgroundCreator
from BL.VideoParts.FrontCreator.TextCreator.TextCreator import TextCreator
from BL.VideoParts.FrontCreator.TextCreatorManager.TextCreatorManager import TextCreatorManager
from Configurations.Configuration import Configuration
from Pullers.BackgroundPuller.VideoBackgroundPuller import VideoBackgroundPuller
from Pullers.FrontContentPuller.TextPuller.STTPuller.STTPuller import STTPuller
from Pullers.FrontContentPuller.TextPuller.STTPuller.WhisperSTTPuler import WhisperSTTPuller


class AndrewTateBot(BotFactoryBase):

    def __init__(self, config: Configuration):
        super().__init__(config)

    def create_bot(self,) -> IVideoConnector:
        text_puller = WhisperSTTPuller()
        background_puller = VideoBackgroundPuller(self.config.background_configuration)
        background_creator = BackgroundCreator(background_puller, self.config.video_connector_configuration)
        text_creator = TextCreator()
        text_creator_manager = TextCreatorManager(text_creator, text_puller)
        text_video_connector = TextVideoConnector(background_puller, background_creator, self.config.video_connector_configuration, text_creator_manager)

        return text_video_connector
