from BL.VideoParts.FrontCreator.ImageTextCreator.IImageTextCreator import IImageTextCreator


class ImageTextFactory:

    def __init__(self, image_creator: IImageTextCreator):
        self.image_creator = image_creator
        self.submission_to_data = {}

    def create_images_text(self, submission: str, number: int = None) -> list[list[str], list[str]]:
        if submission not in self.submission_to_data or len(self.submission_to_data[submission]) != number:
            images_texts = self.image_creator.create_image_text(submission, number)

            images, texts = [], []

            for image_text in images_texts:
                images.append(image_text.path)
                texts.append(image_text.text)

            self.submission_to_data[submission] = [images, texts]

        return self.submission_to_data[submission]
