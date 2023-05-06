import pytube
from praw import Reddit

from BL.Factory.BotFactory.AndrewTateBot import AndrewTateBot
from BL.Factory.BotFactory.RedditCommentBackgroundFactory import RedditCommentBackgroundFactory
from BL.VideoConnector.ImageVoiceConnector.ImageVoiceConnector import ImageVoiceConnector
from BL.VideoConnector.VideoConnector import VideoConnector
from BL.VideoParts.BackgroundCreator.BackgroundCreator import BackgroundCreator
from BL.VideoParts.FrontCreator.ImageCreator.CommentImageCreator import CommentImageCreator
from BL.VideoParts.FrontCreator.ImageTextCreator.ImageTextWebCreator import ImageTextWebCreator
from BL.VideoParts.VoiceCreator.VoiceCreator import VoiceCreator
from Common.Factory.ImageWebPullerModelFactory.ImageWebPullerModelFactory import ImageWebPullerModelFactory
from Configurations.Configuration import Configuration
from Configurations.ConfigurationLoader import load_configuration

from Pullers.BackgroundPuller.VideoBackgroundPuller import VideoBackgroundPuller
from Pullers.FrontContentPuller.ImagePuller.WebImagePuller import WebImagePuller
from Pullers.FrontContentPuller.MetaDataPuller.CommentPuller.ReddictCommentPuller import RedditCommentPuller
from Pullers.FrontContentPuller.MetaDataPuller.RedditPuller.SubmissionPuller import SubmissionPuller
from Pullers.FrontContentPuller.TextPuller.STTPuller.STTPuller import STTPuller
from Pullers.VoicePuller.CustomVoicePuller import CustomVoicePuller
from Pullers.VoicePuller.MultipleVoicesPuller.MultipleVoicePuller import MultipleVoicePuller

# Crating Configuration

config = load_configuration("./Configurations/config.json")

# video_connector_factory = RedditCommentBackgroundFactory(config)
# video_connector = video_connector_factory.create_bot()
#
# video_connector.connect_video(submission="12klzj9",
#                               background="minecraft")

video_connector_factory = AndrewTateBot(config)
video_connector = video_connector_factory.create_bot()
video_connector.connect_video(voice='short', background='minecraft')