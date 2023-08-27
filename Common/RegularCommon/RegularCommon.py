from random import randrange
from typing import Callable, Any, Tuple
import torch.cuda

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


def calc_parabola_vertex(x1, y1, x2, y2, x3, y3):
    denom = (x1 - x2) * (x1 - x3) * (x2 - x3)

    if denom == 0:
        return 0, 0, y3

    a = (x3 * (y2 - y1) + x2 * (y1 - y3) + x1 * (y3 - y2)) / denom
    b = (x3 * x3 * (y1 - y2) + x2 * x2 * (y3 - y1) + x1 * x1 * (y2 - y3)) / denom
    c = (x2 * x3 * (x2 - x3) * y1 + x3 * x1 * (x3 - x1) * y2 + x1 * x2 * (x1 - x2) * y3) / denom

    return a, b, c


def calc_function_string(a: float, b: float, c: float, x_str: str) -> str:
    return f'{a}*{x_str}^2{calc_sign(b)}*{x_str}{calc_sign(c)}'


def calc_sign(x: float) -> str:
    return f'-{abs(x)}' if x < 0 else f'+{x}'


def calc_parabolla_function_from_3_points(x1, y1, x2, y2, x3, y3, x_str: str = 'x') -> str:
    a, b, c = calc_parabola_vertex(x1, y1, x2, y2, x3, y3)

    return calc_function_string(a, b, c, x_str)


def device_avalible() -> str:
    return 'cuda' if torch.cuda.is_available() else None