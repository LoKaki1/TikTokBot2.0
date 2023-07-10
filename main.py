
from BL.Factory.BotFactory.AndrewTateBot import AndrewTateBot
from BL.Factory.BotFactory.FFMpegRedditFactory import FFmpegRedditFactory
from BL.Factory.BotFactory.FFmpegAndrewTateBotCreator import FFmpegAndrewTateBotCreator
from BL.Factory.BotFactory.RedditCommentBackgroundFactory import RedditCommentBackgroundFactory

from Configurations.ConfigurationLoader import load_configuration

# Crating Configuration

config = load_configuration("./Configurations/config.json")


# video_connector_factory = RedditCommentBackgroundFactory(config)
# video_connector = video_connector_factory.create_bot()
#
# video_connector.connect_video(submission="12klzj9",
#                               background="minecraft")
#
# video_connector_factory = AndrewTateBot(config)
# video_connector = video_connector_factory.create_bot()
# video_connector.connect_video(voice='short', background='minecraft')
# video_connector_factory = FFmpegAndrewTateBotCreator(config)
# ffmpeg_bot = video_connector_factory.create_bot()
# ffmpeg_bot.connect_video(voice='short', background='minecraft')
video_connector_factory = FFmpegRedditFactory(config)
creator = video_connector_factory.create_bot()
creator.connect_video(submission="14teirv",
                      background="minecraft")
