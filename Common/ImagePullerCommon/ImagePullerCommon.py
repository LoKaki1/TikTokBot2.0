import re
from os import path, mkdir
import urllib.request
from typing import List

import requests

from Common.LoggerCommon.Logger import log_error, log_info


def generate_image_xpath(index: int):
    return IMAGE_XPATH.format(index=index)


def generate_image_path(image_name: str):
    if not path.exists(IMAGES_FOLDER):
        mkdir(IMAGES_FOLDER)

    return f'{IMAGES_FOLDER}/{image_name}.jpg'


def download_src(image_source, image_path):
    opener = urllib.request.URLopener()
    opener.addheader('User-Agent', 'Mozilla/5.0')
    opener.retrieve(image_source, image_path)


def download_image(image_source: str, image_path: str):
    image_path = f'{IMAGES_FOLDER}/{id(image_path)}.jpg'

    try:
        download_src(image_source, image_path)

        return image_path

    except Exception as e:
        log_error(f'failed downloading path for image: {image_path}\nerror: {e}', AssertionError, False)

        image_path = f'{IMAGES_FOLDER}/{id(image_path)}.jpg'
        download_src(image_source, image_path)

        return image_path


def search(image_search: str):
    return requests.get(
        GOOGLE_IMAGE_URL.format(image_search=image_search), headers=GOOGLE_HEADERS)


def url_formatting_regex(url: str):
    regexes = ['.png', '.jpg', '.bmp', '.jpeg', '.svg']
    regex_expression = "(" + ")|(".join(regexes) + ")"

    return re.findall(regex_expression, url) and 'encrypted' not in url


def get_image_data(image_search: str):
    "Idan mevaes"

    image_search = image_search.replace(' ', '+')
    data = search(image_search)
    data = data.text.split(SCRIPT_SPLIT)[-1]

    return data


def get_srcs_from_search(image_search: str) -> List[str]:
    data = get_image_data(image_search)
    data = re.findall(REGEX_EXPRESSION, data)
    log_info(f"After Regex: {data}")
    data = [f"{protocol}://{url}{rest}" for (protocol, url, rest) in data if url_formatting_regex(rest)]
    log_info(f'After Logic: {data}')

    return data


GOOGLE_INPUT_XPATH = '//input[@class="gLFyf"]'
GOOGLE_SEARCH_BUTTON = '//button[@jsname="Tg7LZd" or @class="Tg7LZd"]'

IMAGE_XPATH = '//*[@id="islrg"]/div[1]/div[{index}]/a[1]/div[1]/img'

IMAGE_SRC_XPATH = '//*[@id="Sva75c"]//c-wiz/div[2]//img[@class="n3VNCb KAlRDb"]'
IMAGES_FOLDER = './images'
GOOGLE_HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }

GOOGLE_IMAGE_URL = 'https://www.google.com/search?q={image_search}&tbm=isch&sxsrf=ALiCzsYC0g7U' \
                   '7H9ensWwVTW8AWjcevBgBA%3A1672423108601&source=hp&biw=1920&bih=937&ei=xCavY' \
                   '_TlIfmZkdUPzqGUgAI&iflsig=AJiK0e8AAAAAY6801GZeQQs3xF1ZTYq_np4LOKoRNHdX&ved' \
                   '=0ahUKEwj017LK9aH8AhX5TKQEHc4QBSAQ4dUDCAc&uact=5&oq=olympic&gs_lcp=CgNpbWc' \
                   'QAzIECCMQJzIECAAQQzIECAAQQzIECAAQQzIECAAQQzIECAAQQzIECAAQQzIECAAQQzIECAAQQ' \
                   'zIECAAQQ1AAWABgrRxoAXAAeACAAX6IAX6SAQMwLjGYAQCqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img'

REGEX_EXPRESSION = r"(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])"
SCRIPT_SPLIT = """AF_initDataCallback({key: 'ds:1', hash: '2', data:"""
