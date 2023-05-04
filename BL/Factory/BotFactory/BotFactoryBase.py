from BL.VideoConnector.IVideoConnector import IVideoConnector
from Configurations.Configuration import Configuration


class BotFactoryBase:
    def __init__(self, config: Configuration):
        self.config = config
        self.reddit_configuration = config.reddit_configuration
        self.voice_configuration = config.voice_configuration
        self.background_configuration = config.background_configuration
        self.video_connector_configuration = config.video_connector_configuration
        self.image_puller_configuration = config.image_puller_configuration

    def create_bot(self,) -> IVideoConnector:
        """
        :return:
        """