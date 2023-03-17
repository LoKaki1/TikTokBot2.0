from BL.VideoParts.BackgroundCreator.IBackgroundCreator import IBackgroundCreator
from Common.LoggerCommon.Logger import logger_info_decorator


class BackgroundCreator(IBackgroundCreator):

    @logger_info_decorator
    def create_background(self, *args, **kwargs):
        """
        :param args:
        :param kwargs:
        :return:
        """