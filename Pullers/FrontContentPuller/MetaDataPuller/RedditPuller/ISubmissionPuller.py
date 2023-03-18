from praw.models import Submission


class ISubmissionPuller:

    def pull_submission(self, submission: str) -> Submission:
        """
        :param submission:
        :return:
        """