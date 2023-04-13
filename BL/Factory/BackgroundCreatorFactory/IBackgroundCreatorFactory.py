from BL.VideoParts.BackgroundCreator.IBackgroundCreator import IBackgroundCreator


class IBackgroundCreatorFactory:

    def create_background_creator(self) -> IBackgroundCreator:
        """
        :return:
        """