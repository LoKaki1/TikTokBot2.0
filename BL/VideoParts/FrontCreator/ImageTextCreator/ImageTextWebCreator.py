from BL.VideoParts.FrontCreator.ImageTextCreator.IImageTextCreator import IImageTextCreator
from Common.LoggerCommon.Logger import logger_info_decorator
from Common.Models.ImageTextModel import ImageTextModel


class ImageTextWebCreator(IImageTextCreator):

    @logger_info_decorator
    def create_image_text(self, *args, **kwargs) -> ImageTextModel:
        """
        :param args:
        :param kwargs:
        :return:
        """

