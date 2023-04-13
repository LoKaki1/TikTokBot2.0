from BL.VideoParts.FrontCreator.ImageTextCreator.IImageTextCreator import IImageTextCreator


class IFrontCreatorFactory:

    def create_front_creator(self) -> IImageTextCreator:
        """
        :return:
        """