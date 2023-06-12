import time
from typing import List

from playwright.sync_api import Page, sync_playwright

from Common.LoggerCommon.Logger import logger_info_decorator
from Common.Models.ImageWebPullerModel import ImageWebPullerModel
from Configurations.ImagePullerConfiguration.ImagePullerConfiguration import ImagePullerConfiguration
from Pullers.FrontContentPuller.ImagePuller.IImagePuller import IImagePuller


class WebImagePuller(IImagePuller):

    def __init__(self, config: ImagePullerConfiguration):
        self.config = config

    @logger_info_decorator
    def pull_images(self, images_web_puller_model: List[ImageWebPullerModel]) -> List[str]:
        """
        :return:
        """
        with sync_playwright() as play_write:
            browser = play_write.chromium.launch(headless=True)  # headless=False #to check for chrome view
            context = browser.new_context()
            page = context.new_page()

            screenshots = [self._download_screenshot(model.page_link, model.xpath, model.path, page)
                           for model in images_web_puller_model]

            return screenshots

    def _download_screenshot(self,
                             page_link: str,
                             xpath: str,
                             path_to_save: str,
                             page: Page) -> str:
        page.goto(page_link, timeout=self.config.timeout)
        zoom = 1.4
        page.evaluate(f"document.body.style.zoom={zoom}")
        locator = page.locator(xpath)
        locator.scroll_into_view_if_needed()
        location = locator.bounding_box()
        page.eval_on_selector(f"//div[@class='side']", "el => el.setAttribute('style','display:none')")

        for i in location:
            location[i] = float("{:.2f}".format(location[i] * zoom))

        page.screenshot(clip=location, path=path_to_save)

        return path_to_save
