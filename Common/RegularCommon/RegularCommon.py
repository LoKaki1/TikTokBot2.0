from random import randrange
from typing import Callable, Any, Tuple


def remove_where(iterate_list: list, removed_list: list, where_func: Callable[[Any], bool]):
    removed_list = removed_list.copy()
    iterate_list_copy = iterate_list.copy()

    for index, comment in enumerate(iterate_list):
        if where_func(comment):
            removed_list.pop(index)
            iterate_list_copy.pop(index)

    return removed_list, iterate_list_copy


def generate_video_start_end(video_duration: int, length: int) -> Tuple[int, int]:
    if length is None or length >= video_duration:
        return 0, video_duration

    return (random_time := randrange(0, int(video_duration - length))), random_time + length


def get_name_from_path(url: str) -> str:
    return url.split('/')[-1]


def split_youtube_url(url: str) -> str:
    if 'shorts' in url:
        video_name = url.split('shorts')[-1]
    else:
        video_name = url.split('watch?v=')[-1]

    return video_name.replace('/', '')
