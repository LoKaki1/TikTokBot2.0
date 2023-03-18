from Common.Factory.ImageWebPullerModelFactory.IImageWebPullerModelFactory import IImageWebPullerModelFactory
from Common.Models.ImageWebPullerModel import ImageWebPullerModel
from Configurations.RedditConfiguration.RedditConfiguration import RedditConfiguration


class ImageWebPullerModelFactory(IImageWebPullerModelFactory):

    def __init__(self,
                 reddit_config: RedditConfiguration
                 ):
        self.reddit_config = reddit_config

    def create_image_web_model(self, comment) -> ImageWebPullerModel:
        return ImageWebPullerModel(
            self.reddit_config.comment_url.format(comment.permalink),
            self.reddit_config.comment_locator.format(comment.id),
            self.reddit_config.comments_path.format(comment.id)
        )
