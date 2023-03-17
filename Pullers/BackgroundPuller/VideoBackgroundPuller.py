from Common.LoggerCommon.Logger import logger_info_decorator
from Pullers.BackgroundPuller.IBackgroundPuller import IBackgroundPuller


class VideoBackgroundPuller(IBackgroundPuller):

    @logger_info_decorator
    def pull_background(self, *args, **kwargs) -> str:
        """
        :param args:
        :param kwargs:
        :return:
        """