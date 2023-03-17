from Common.LoggerCommon.Logger import logger_info_decorator
from Common.Models.ImageTextModel import ImageTextModel
from Common.Models.ImageWebPullerModel import ImageWebPullerModel
from Pullers.FrontContentPuller.ImageTextPuller.IImageTextPuller import IImageTextPuller


class ImageWebTextPuller(IImageTextPuller):

    def __init__(self, reddit_praw):
        self.reddit_praw = reddit_praw

    @logger_info_decorator
    def pull_image_text(self, image_web_model: ImageWebPullerModel) -> ImageTextModel:
        """
        :param image_web_model:
        :return:
        """