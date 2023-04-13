from praw.reddit import Comment, Submission

from BL.VideoParts.FrontCreator.ImageCreator.IImageCreator import IImageCreator
from BL.VideoParts.FrontCreator.ImageTextCreator.IImageTextCreator import IImageTextCreator
from Common.LoggerCommon.Logger import logger_info_decorator
from Common.Models.ImageTextModel import ImageTextModel
from Pullers.FrontContentPuller.MetaDataPuller.CommentPuller.ICommentsPuller import ICommentPuller
from Pullers.FrontContentPuller.MetaDataPuller.RedditPuller.ISubmissionPuller import ISubmissionPuller


class ImageTextWebCreator(IImageTextCreator):

    def __init__(self,
                 image_creator: IImageCreator,
                 comment_puller: ICommentPuller,
                 submission_puller: ISubmissionPuller,
                 ):
        self.submission_puller = submission_puller
        self.comment_puller = comment_puller
        self.image_creator = image_creator
        self.text_from_image = {
            Submission: lambda x: x.title,
            Comment: lambda x: x.body
        }

    @logger_info_decorator
    def create_image_text(self, submission: str) -> list[ImageTextModel]:
        """
        :return:
        """
        submission = self.submission_puller.pull_submission(submission)
        comments = self.comment_puller.pull_comments(submission)
        images_path = self.image_creator.create_images(comments)

        image_text_model = [
            ImageTextModel(
                image_path, self.text_from_image.get(type(comment), Comment)(comment)
            ) for image_path, comment in zip(images_path, comments)
        ]

        return image_text_model





