import os
import pathlib


def write_file(path: str, message: str):
    with open(path, 'a') as file:
        file.write(f"\n{message}")


def delete_file(path: str):
    pathlib_path = pathlib.Path(path)
    pathlib_path.unlink()


def save_dir(path: str) -> bool:
    if not (created := os.path.exists(path)):
        os.makedirs(path)

    return created

