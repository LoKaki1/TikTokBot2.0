from BL.VideoParts.VoiceCreator.IVoiceCreator import IVoiceCreator


class IVoiceCreatorFactory:

    def create_voice_creator(self) -> IVoiceCreator:
        """
        :return:
        """
