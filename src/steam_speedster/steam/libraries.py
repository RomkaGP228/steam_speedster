from pathlib import Path


def get_steam_libraries(steam_path: Path | str) -> list:
    """Функция для получения всех директорий с играми и файлами STEAM

        Args:
            steam_path: Path, str

        Returns:
            libraries: list
    """
    libraries = list()
    steam_path = Path(steam_path)
    libraries.append(steam_path)
    vdf_folder_path = steam_path / "steamapps" / "libraryfolders.vdf"
    if not vdf_folder_path:
        return libraries
    with open(vdf_folder_path, mode="r", encoding="utf-8") as f:
        data = f.readlines()
        for i in data:
            line = i.strip().split('"')
            if '"path"' in i.strip():
                new_path = line[3].replace('    \\\\', '\\')
                libraries.append(Path(new_path))
    return libraries
