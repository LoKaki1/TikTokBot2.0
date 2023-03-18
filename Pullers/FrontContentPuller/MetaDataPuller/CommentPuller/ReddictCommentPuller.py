from typing import Any

from praw.models import Submission

from Common.LoggerCommon.Logger import logger_info_decorator
from Pullers.FrontContentPuller.MetaDataPuller.CommentPuller.ICommentsPuller import ICommentPuller


class RedditCommentPuller(ICommentPuller):

    @logger_info_decorator
    def pull_comments(self, submission: Submission) -> list[Any]:
        """
        :return:
        """

        return submission.comments.list()

