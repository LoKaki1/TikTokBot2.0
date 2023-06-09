from dataclasses import dataclass
from dataclasses_json import dataclass_json, LetterCase

from Configurations.BackgroundConfiguration.BackgroundConfiguration import BackgroundConfiguration
from Configurations.ImagePullerConfiguration.ImagePullerConfiguration import ImagePullerConfiguration
from Configurations.RedditConfiguration.RedditConfiguration import RedditConfiguration
from Configurations.VideoConnectorConfiguration.VideoConnectorConfiguration import VideoConnectorConfiguration
from Configurations.VoiceConfiguration.VoiceConfiguration import VoiceConfiguration


@dataclass_json(letter_case=LetterCase.PASCAL)
@dataclass
class Configuration:
    background_configuration: BackgroundConfiguration
    reddit_configuration: RedditConfiguration
    voice_configuration: VoiceConfiguration
    video_connector_configuration: VideoConnectorConfiguration
    image_puller_configuration: ImagePullerConfiguration
