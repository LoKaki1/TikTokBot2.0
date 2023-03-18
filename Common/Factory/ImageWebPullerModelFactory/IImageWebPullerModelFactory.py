from Common.Models.ImageWebPullerModel import ImageWebPullerModel


class IImageWebPullerModelFactory:

    def create_image_web_model(self, comment) -> ImageWebPullerModel:
        """
        :param comment:
        :return:
        """