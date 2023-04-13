from BL.Factory.BackgroundCreatorFactory.IBackgroundCreatorFactory import IBackgroundCreatorFactory
from BL.VideoParts.BackgroundCreator.IBackgroundCreator import IBackgroundCreator
from Configurations.BackgroundConfiguration.BackgroundConfiguration import BackgroundConfiguration


class BackgroundCreatorFactory(IBackgroundCreatorFactory):

    def __int__(self, config: BackgroundConfiguration):
        self.config = config

    def create_background_creator(self) -> IBackgroundCreator:
        """
        :return:
        """
