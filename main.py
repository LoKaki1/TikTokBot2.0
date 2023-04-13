from praw import Reddit

from BL.VideoConnector.ImageVoiceConnector.ImageVoiceConnector import ImageVoiceConnector
from BL.VideoConnector.VideoConnector import VideoConnector
from BL.VideoParts.BackgroundCreator.BackgroundCreator import BackgroundCreator
from BL.VideoParts.FrontCreator.ImageCreator.CommentImageCreator import CommentImageCreator
from BL.VideoParts.FrontCreator.ImageTextCreator.ImageTextWebCreator import ImageTextWebCreator
from BL.VideoParts.VoiceCreator.VoiceCreator import VoiceCreator
from Common.Factory.ImageWebPullerModelFactory.ImageWebPullerModelFactory import ImageWebPullerModelFactory
from Configurations.ConfigurationLoader import load_configuration

from Pullers.BackgroundPuller.VideoBackgroundPuller import VideoBackgroundPuller
from Pullers.FrontContentPuller.ImagePuller.WebImagePuller import WebImagePuller
from Pullers.FrontContentPuller.MetaDataPuller.CommentPuller.ReddictCommentPuller import RedditCommentPuller
from Pullers.FrontContentPuller.MetaDataPuller.RedditPuller.SubmissionPuller import SubmissionPuller
from Pullers.VoicePuller.CustomVoicePuller import CustomVoicePuller
from Pullers.VoicePuller.MultipleVoicesPuller.MultipleVoicePuller import MultipleVoicePuller

# Crating Configuration

config = load_configuration("./Configurations/config.json")

reddit_configuration = config.reddit_configuration
voice_configuration = config.voice_configuration
background_configuration = config.background_configuration
video_connector_configuration = config.video_connector_configuration
image_puller_configuration = config.image_puller_configuration

# Creating Praw

reddit_praw = Reddit(
    user_agent=reddit_configuration.user_agent,
    client_secret=reddit_configuration.client_secret,
    client_id=reddit_configuration.client_id
)

# Creating Factories

image_web_puller_model_factory = ImageWebPullerModelFactory(reddit_configuration)

# Creating Pullers

background_puller = VideoBackgroundPuller(background_configuration)
image_puller = WebImagePuller(image_puller_configuration)
submission_puller = SubmissionPuller(reddit_praw)
comment_puller = RedditCommentPuller(reddit_configuration)
voice_puller = CustomVoicePuller(voice_configuration)

# Creating Creators

background_creator = BackgroundCreator(background_puller, video_connector_configuration)
image_creator = CommentImageCreator(image_puller, image_web_puller_model_factory)
image_text_creator = ImageTextWebCreator(image_creator, comment_puller, submission_puller)
voice_creator = VoiceCreator(voice_configuration, voice_puller)

# Creating Connectors

image_voice_connector = ImageVoiceConnector(video_connector_configuration, image_text_creator, voice_creator)
video_connector = VideoConnector(video_connector_configuration, background_creator, image_voice_connector)

video_connector.connect_video(submission="12klzj9",
                              background="minecraft")
