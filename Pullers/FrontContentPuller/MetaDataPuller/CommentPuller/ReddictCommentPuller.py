from typing import Any

from praw.models import Submission, MoreComments

from Common.LoggerCommon.Logger import logger_info_decorator
from Configurations.RedditConfiguration.RedditConfiguration import RedditConfiguration
from Pullers.FrontContentPuller.MetaDataPuller.CommentPuller.ICommentsPuller import ICommentPuller


class RedditCommentPuller(ICommentPuller):
    def __init__(self, reddit_configuration: RedditConfiguration):
        self.config = reddit_configuration
        self.not_legit_comment_strings = self.config.string_not_in_comments
        self.submissions_comments = {}

    @logger_info_decorator
    def pull_comments(self, submission: Submission) -> list[Any]:
        """
        :return:
        """
        if submission.id not in self.submissions_comments:
            submission_comments = submission.comments.list()
            self.submissions_comments[submission.id] = current_submission_comments = [submission]
            # This for putting the title like other comments

            for submission_comment in submission_comments:
                if len(current_submission_comments) > self.config.number_of_comments:
                    break

                if self._is_legit_comment(submission_comment):
                    current_submission_comments.append(submission_comment)

        return self.submissions_comments[submission.id]

    def _is_legit_comment(self, comment) -> bool:
        return all([not_legit_string not in comment.body for not_legit_string in self.not_legit_comment_strings]) \
               and len(comment.body.split(' ')) <= 20 \
               and len(comment.replies.list()) == 0
