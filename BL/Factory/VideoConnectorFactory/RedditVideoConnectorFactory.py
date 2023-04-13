from BL.Factory.VideoConnectorFactory.IVideoConnectorFactory import IVideoConnectorFactory
from BL.VideoConnector.IVideoConnector import IVideoConnector
from Configurations.Configuration import Configuration


class RedditVideoConnectorFactory(IVideoConnectorFactory):

    def __init__(self, config: Configuration):
        self.config = config

    def create_video_connector(self, *args, **kwargs) -> IVideoConnector:
        """
        :param args:
        :param kwargs:
        :return:
        """
