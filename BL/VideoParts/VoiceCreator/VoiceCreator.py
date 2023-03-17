from typing import List

from BL.VideoParts.VoiceCreator.IVoiceCreator import IVoiceCreator
from Common.LoggerCommon.Logger import logger_info_decorator


class VoiceCreator(IVoiceCreator):

    @logger_info_decorator
    def create_voice(self, *args, **kwargs) -> List[str]:
        """
        :return:
        """