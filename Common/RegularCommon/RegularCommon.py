from typing import Callable, Any


def remove_where(iterate_list: list, removed_list: list, where_func: Callable[[Any], bool]):
    removed_list = removed_list.copy()
    iterate_list_copy = iterate_list.copy()

    for index, comment in enumerate(iterate_list):
        if where_func(comment):
            removed_list.pop(index)
            iterate_list_copy.pop(index)

    return removed_list, iterate_list_copy
