from typing import Any

from praw.models import Submission


class ICommentPuller:

    def pull_comments(self, submission: Submission) -> list[Any]:
        """
        :return:
        """