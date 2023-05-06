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

    return (random_time := randrange(0, video_duration)), random_time + length
