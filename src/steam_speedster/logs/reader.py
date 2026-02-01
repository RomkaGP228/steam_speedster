from pathlib import Path


def read_new_lines(file_path: str | Path, last_position: int):
    """Функция для прочтения строк из файла, который указан.
        Args:
            file_path: str | Path
            last_position: int
        Returns:
            list(str), int"""
    with open(file_path, "r", encoding="utf-8") as f:
        f.seek(last_position)
        lines = f.readlines()
        new_position = f.tell()

    return lines, new_position
