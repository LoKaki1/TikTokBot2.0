from dataclasses import dataclass
from typing import List

from dataclasses_json import dataclass_json, LetterCase


@dataclass_json(letter_case=LetterCase.PASCAL)
@dataclass
class RedditConfiguration:
    client_id: str
    client_secret: str
    user_agent: str
    comments_path: str
    comment_path_format: str
    comment_url: str
    comment_locator: str
    title_locator: str
    number_of_comments: int
    string_not_in_comments: List[str]
