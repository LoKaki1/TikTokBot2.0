from typing import Any

from BL.VideoParts.FrontCreator.ImageCreator.IImageCreator import IImageCreator
from Common.Factory.ImageWebPullerModelFactory.IImageWebPullerModelFactory import IImageWebPullerModelFactory
from Common.LoggerCommon.Logger import logger_info_decorator
from Pullers.FrontContentPuller.ImagePuller.IImagePuller import IImagePuller


class CommentImageCreator(IImageCreator):

    def __init__(self,
                 image_puller: IImagePuller,
                 comment_image_web_model_factory: IImageWebPullerModelFactory
                 ):
        self.comment_image_web_model_factory = comment_image_web_model_factory

        self.image_puller = image_puller

    @logger_info_decorator
    def create_images(self, comments: list[Any]):
        """
        :return:
        """
        model = [
            self.comment_image_web_model_factory.create_image_web_model(comment)
            for comment in comments
        ]

        images_path = self.image_puller.pull_images(model)

        return images_path
