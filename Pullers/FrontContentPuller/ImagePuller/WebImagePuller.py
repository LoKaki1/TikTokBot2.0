from Common.LoggerCommon.Logger import logger_info_decorator
from Pullers.FrontContentPuller.ImagePuller.IImagePuller import IImagePuller


class WebImagePuller(IImagePuller):

    @logger_info_decorator
    def pull_image(self, *args, **kwargs) -> str:
        """
        :param args:
        :param kwargs:
        :return:
        """