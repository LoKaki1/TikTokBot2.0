from typing import List

from Common.Models.ImageWebPullerModel import ImageWebPullerModel


class IImagePuller:

    def pull_images(self, images_web_puller_model: List[ImageWebPullerModel]) -> List[str]:
        """
        :return:
        """