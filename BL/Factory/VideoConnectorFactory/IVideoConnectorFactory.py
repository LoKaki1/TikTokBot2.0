from BL.VideoConnector.IVideoConnector import IVideoConnector


class IVideoConnectorFactory:

    def create_video_connector(self, *args, **kwargs) -> IVideoConnector:
        """
        :param args:
        :param kwargs:
        :return:
        """