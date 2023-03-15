from dataclasses import dataclass


@dataclass
class ImageWebPullerModel:
    page_link: str
    xpath: str
    path: str
