from typing import List

from Common.LoggerCommon.Logger import logger_info_decorator
from Configurations.VoiceConfiguration.VoiceConfiguration import VoiceConfiguration
from Pullers.VoicePuller.IVoicePuller import IVoicePuller


class MultipleVoicePuller(IVoicePuller):

    def __init__(self, configuration: VoiceConfiguration):
        self.config = configuration

    @logger_info_decorator
    def pull_voice(self, texts: List[str], voice: str) -> List[str]:
        """
        :param voice:
        :param texts:
        :return:
        """