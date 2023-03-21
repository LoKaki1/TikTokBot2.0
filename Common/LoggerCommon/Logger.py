import datetime
import logging
from typing import Type

FILE = './Logs/Logs.txt'


def log_info(message: str):
    message = f"{datetime.datetime.now().strftime('%Y-%m-%d  %H:%M:%S')}: {message}"
    print(message)


def logger_info_decorator(function):
    def wrapper(*args, **kwargs):
        log_info(f"Function {function.__name__}: with arguments: {args, kwargs}")
        result = function(*args, **kwargs)
        log_info(f"Resulted: {result}")

        return result

    return wrapper


logger_types = {
    'info': log_info,
    'error': logging.error,
    'debug': logging.debug
}


def log(message: str, type_of_log: str):
    logger_types[type_of_log](message)


def log_error(message: str, exception: Type[BaseException], to_raise: bool = True):
    log(message, 'error')

    if to_raise:
        raise exception(message)


def log_info(message):
    log(message, 'info')


def log_debug(message: str):
    log(message, 'debug')
