from Common.Models.ImageTextModel import ImageTextModel


class IImageTextCreator:

    def create_image_text(self, submission: str) -> list[ImageTextModel]:
        """
        :return:
        """