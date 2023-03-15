from Pullers.FrontContentPuller.ImagePuller.IImagePuller import IImagePuller


class WebImagePuller(IImagePuller):

    def pull_image(self, *args, **kwargs) -> str:
        """
        :param args:
        :param kwargs:
        :return:
        """