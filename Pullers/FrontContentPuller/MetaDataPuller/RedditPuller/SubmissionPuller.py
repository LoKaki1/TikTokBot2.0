from praw import Reddit
from praw.models import Submission

from Pullers.FrontContentPuller.MetaDataPuller.RedditPuller.ISubmissionPuller import ISubmissionPuller


class SubmissionPuller(ISubmissionPuller):

    def __init__(self, reddit_parw: Reddit):
        self.redit_praw = reddit_parw
        self.submission = None

    def pull_submission(self, submission: str) -> Submission:
        if self.submission is None or self.submission.id != submission:
            self.submission = self.redit_praw.submission(submission)

        return self.submission
