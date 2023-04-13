from BL.Factory.FrontCreatorFactory.IFrontCreatorFactory import IFrontCreatorFactory
from BL.VideoParts.FrontCreator.ImageTextCreator.IImageTextCreator import IImageTextCreator
from Configurations.ImagePullerConfiguration.ImagePullerConfiguration import ImagePullerConfiguration


class FrontCreatorFactory(IFrontCreatorFactory):

    def __init__(self, image_configuration: ImagePullerConfiguration):
        self.image_configuration = image_configuration

    def create_front_creator(self) -> IImageTextCreator:
        """
        :return:
        """