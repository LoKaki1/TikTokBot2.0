
from BL.Factory.BotFactory.AndrewTateBot import AndrewTateBot
from Configurations.ConfigurationLoader import load_configuration

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