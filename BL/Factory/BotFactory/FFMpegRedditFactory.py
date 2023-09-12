from praw import Reddit

from BL.Factory.BotFactory.BotFactoryBase import BotFactoryBase
from BL.Factory.MetadataFactory.ImageTextFactory import ImageTextFactory
from BL.VideoConnector.FFMpegRedditTextConnector import FFMpegRedditTextConnector
from BL.VideoConnector.FFmpegRedditVideoConnector import FFmpegRedditVideoConnector
from BL.VideoConnector.IVideoConnector import IVideoConnector
from BL.VideoParts.BackgroundCreator.FFmpegBackgroundCreator import FFmpegBackgroundCreator
from BL.VideoParts.FrontCreator.FFMpegFrontCreator.FFMpegTextCreator.DrawText.DrawText import DrawText
from BL.VideoParts.FrontCreator.FFMpegFrontCreator.FFmpegImageCreator.OverlayImages import OverlayImages
from BL.VideoParts.FrontCreator.ImageCreator.CommentImageCreator import CommentImageCreator
from BL.VideoParts.FrontCreator.ImageTextCreator.ImageTextWebCreator import ImageTextWebCreator
from BL.VideoParts.VoiceCreator.VoiceCreator import VoiceCreator
from Common.Factory.ImageWebPullerModelFactory.ImageWebPullerModelFactory import ImageWebPullerModelFactory
from Common.Factory.STTModelFactory.STTModelFactory import STTModelFactory
from Pullers.BackgroundPuller.VideoBackgroundPuller import VideoBackgroundPuller
from Pullers.FrontContentPuller.ImagePuller.WebImagePuller import WebImagePuller
from Pullers.FrontContentPuller.MetaDataPuller.CommentPuller.ReddictCommentPuller import RedditCommentPuller
from Pullers.FrontContentPuller.MetaDataPuller.RedditPuller.SubmissionPuller import SubmissionPuller
from Pullers.FrontContentPuller.TextPuller.STTPuller.STTPullerProxy import STTPullerProxy
from Pullers.FrontContentPuller.TextPuller.STTPuller.WhisperSTTPuler import WhisperSTTPuller
from Pullers.VideoDonwloaderPuller.YoutubeVideoDownloaderPuller import YoutubeVideoDownloaderPuller
from Pullers.VoicePuller.CustomVoicePuller import CustomVoicePuller


class FFmpegRedditFactory(BotFactoryBase):

    def create_bot(self,) -> IVideoConnector:
        # Creating Praw
        reddit_praw = Reddit(
            user_agent=self.reddit_configuration.user_agent,
            client_secret=self.reddit_configuration.client_secret,
            client_id=self.reddit_configuration.client_id
        )

        # Creating Factories

        image_web_puller_model_factory = ImageWebPullerModelFactory(self.reddit_configuration)

        # Creating Pullers
        downloader_puller = YoutubeVideoDownloaderPuller(self.config.background_configuration)
        background_puller = VideoBackgroundPuller(self.background_configuration, downloader_puller)
        image_puller = WebImagePuller(self.image_puller_configuration)
        submission_puller = SubmissionPuller(reddit_praw)
        comment_puller = RedditCommentPuller(self.reddit_configuration, 0)
        voice_puller = CustomVoicePuller(self.voice_configuration)

        # Creating Creators

        background_creator = FFmpegBackgroundCreator(background_puller, self.video_connector_configuration)
        image_creator = CommentImageCreator(image_puller, image_web_puller_model_factory)
        image_text_creator = ImageTextWebCreator(image_creator, comment_puller, submission_puller)
        voice_creator = VoiceCreator(self.voice_configuration, voice_puller)
        image_text_factory = ImageTextFactory(image_text_creator)
        overlay_images = OverlayImages(self.config.video_connector_configuration,
                                       image_text_creator,
                                       voice_creator,
                                       image_text_factory)
        draw_text = DrawText()
        stt_model_factory = STTModelFactory()
        stt_puller = WhisperSTTPuller(self.config.stt_configuration, stt_model_factory)
        stt_puller = STTPullerProxy(stt_puller)

        return FFMpegRedditTextConnector(background_creator,
                                         self.video_connector_configuration,
                                         voice_creator,
                                         overlay_images,
                                         image_text_factory,
                                         voice_puller,
                                         self.voice_configuration,
                                         draw_text,
                                         stt_model_factory,
                                         stt_puller)
