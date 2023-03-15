from Pullers.BackgroundPuller.IBackgroundPuller import IBackgroundPuller


class VideoBackgroundPuller(IBackgroundPuller):

    def pull_background(self, *args, **kwargs) -> str:
        """
        :param args:
        :param kwargs:
        :return:
        """