from BL.VideoParts.FrontCreator.ImageCreator.IImageCreator import IImageCreator
from Common.LoggerCommon.Logger import logger_info_decorator


class ImageCreator(IImageCreator):

    @logger_info_decorator
    def create_image(self, *args, **kwargs):
        """
        :param args:
        :param kwargs:
        :return:
        """