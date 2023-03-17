from BL.VideoConnector.IVideoConnector import IVideoConnector
from Common.LoggerCommon.Logger import logger_info_decorator


class VideoConnector(IVideoConnector):

    @logger_info_decorator
    def connect_video(self, *args, **kwargs):
        """
        :param args:
        :param kwargs:
        :return:
        """
