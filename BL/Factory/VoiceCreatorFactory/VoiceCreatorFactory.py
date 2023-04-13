from BL.Factory.VoiceCreatorFactory.IVoiceCreatorFactory import IVoiceCreatorFactory
from BL.VideoParts.VoiceCreator.IVoiceCreator import IVoiceCreator
from Configurations.VoiceConfiguration.VoiceConfiguration import VoiceConfiguration


class VoiceCreatorFactory(IVoiceCreatorFactory):

    def __init__(self, voice_configuration: VoiceConfiguration):
        self.config = voice_configuration

    def create_voice_creator(self) -> IVoiceCreator:
        """
        :return:
        """