from Common.Models.ImageTextModel import ImageTextModel
from Common.Models.ImageWebPullerModel import ImageWebPullerModel
from Pullers.FrontContentPuller.ImageTextPuller.IImageTextPuller import IImageTextPuller


class IImageWebTextPuller(IImageTextPuller):

    def pull_image_text(self, image_web_model: ImageWebPullerModel) -> ImageTextModel:
        """
        :param image_web_model:
        :return:
        """