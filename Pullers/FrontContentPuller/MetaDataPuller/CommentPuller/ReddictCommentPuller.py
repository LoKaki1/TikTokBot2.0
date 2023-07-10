from typing import Any

from praw.models import Submission, MoreComments

from Common.LoggerCommon.Logger import logger_info_decorator
from Configurations.RedditConfiguration.RedditConfiguration import RedditConfiguration
from Pullers.FrontContentPuller.MetaDataPuller.CommentPuller.ICommentsPuller import ICommentPuller


class RedditCommentPuller(ICommentPuller):
    def __init__(self,
                 reddit_configuration: RedditConfiguration,
                 number_of_comments: int):
        self.config = reddit_configuration
        self.not_legit_comment_strings = self.config.string_not_in_comments
        self.submissions_comments = {}
        self.number_of_comments = number_of_comments

    @logger_info_decorator
    def pull_comments(self, submission: Submission, number: int = None) -> list[Any]:
        """
        :return:
        """
        number = number if number is not None else self.number_of_comments

        if submission.id not in self.submissions_comments or \
                len(self.submissions_comments[submission.id]) != number:
            submission_comments = submission.comments.list()
            self.submissions_comments[submission.id] = current_submission_comments = [submission]
            # This for putting the title like other comments

            for submission_comment in submission_comments:
                if len(current_submission_comments) > number:
                    break

                if self._is_legit_comment(submission_comment):
                    current_submission_comments.append(submission_comment)

        return self.submissions_comments[submission.id]

    def _is_legit_comment(self, comment) -> bool:
        return all([not_legit_string not in comment.body for not_legit_string in self.not_legit_comment_strings]) \
               and len(comment.body.split(' ')) <= 20 \
               and len(comment.replies.list()) == 0
